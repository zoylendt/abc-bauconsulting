#!/usr/bin/env bash
set -Eeuo pipefail

cd /workspace

CONFIG_FILE="/workspace/.devcontainer/github.local.yaml" \
GH_SESSION_CONFIG_DIR="/tmp/devcontainer-gh-config" \
python3 - <<'PY'
import os
import re
import subprocess
import sys
from pathlib import Path

import yaml


CONFIG_PATH = Path(os.environ["CONFIG_FILE"])
GH_CONFIG_DIR = Path(os.environ["GH_SESSION_CONFIG_DIR"])
REPOSITORY_PATTERN = re.compile(r"[^/\s]+/[^/\s]+")
BRANCH_PATTERN = re.compile(r"[A-Za-z0-9][A-Za-z0-9._/-]*")


def fail(message: str) -> None:
    print(f"GitHub startup failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def run(
    *args: str,
    input_text: str | None = None,
    environment: dict[str, str] | None = None,
    check: bool = True,
) -> subprocess.CompletedProcess[str]:
    try:
        return subprocess.run(
            args,
            check=check,
            input=input_text,
            text=True,
            capture_output=True,
            env=environment,
        )
    except FileNotFoundError:
        fail(f"required command is not installed: {args[0]}")


def run_checked(
    *args: str,
    input_text: str | None = None,
    environment: dict[str, str] | None = None,
) -> str:
    try:
        result = run(*args, input_text=input_text, environment=environment)
    except subprocess.CalledProcessError as error:
        detail = error.stderr.strip() or error.stdout.strip() or "unknown error"
        fail(f"{' '.join(args)} failed: {detail}")
    return result.stdout.strip()


def command_error(result: subprocess.CompletedProcess[str]) -> str:
    return result.stderr.strip() or result.stdout.strip() or "unknown error"


def session_environment() -> dict[str, str]:
    environment = os.environ.copy()
    environment["GH_CONFIG_DIR"] = str(GH_CONFIG_DIR)
    return environment


def authenticate(repository: str, configured_token: str | None) -> bool:
    GH_CONFIG_DIR.mkdir(mode=0o700, parents=True, exist_ok=True)
    os.chmod(GH_CONFIG_DIR, 0o700)
    environment = session_environment()

    if configured_token:
        login = run(
            "gh",
            "auth",
            "login",
            "--hostname",
            "github.com",
            "--with-token",
            input_text=f"{configured_token}\n",
            environment=environment,
            check=False,
        )
        if login.returncode != 0:
            fail(f"GitHub authentication failed: {command_error(login)}")

    access = run(
        "gh",
        "repo",
        "view",
        repository,
        "--json",
        "nameWithOwner",
        environment=environment,
        check=False,
    )
    if access.returncode != 0:
        if configured_token:
            fail_message = (
                f"the configured token cannot access {repository}: "
                f"{command_error(access)}"
            )
        else:
            fail_message = (
                "no usable GitHub authentication is available to pull "
                f"{repository}; configure github.token or authenticate gh "
                "inside this container session"
            )
        fail(
            fail_message
        )
    return True


def configure_git(repository: str, user_name: str | None, user_email: str | None) -> None:
    if user_name:
        run_checked("git", "config", "--local", "user.name", user_name)
    if user_email:
        run_checked("git", "config", "--local", "user.email", user_email)

    helper = f"!GH_CONFIG_DIR={GH_CONFIG_DIR} gh auth git-credential"
    existing_helpers = run(
        "git",
        "config",
        "--local",
        "--get-all",
        "credential.helper",
        check=False,
    )
    if existing_helpers.returncode == 0 and helper not in existing_helpers.stdout.splitlines():
        run_checked("git", "config", "--local", "--unset-all", "credential.helper")
    run_checked("git", "config", "--local", "credential.helper", helper)

    remote_url = f"https://github.com/{repository}.git"
    remotes = run_checked("git", "remote").splitlines()
    if "origin" not in remotes:
        run_checked("git", "remote", "add", "origin", remote_url)
    elif run_checked("git", "remote", "get-url", "origin") != remote_url:
        run_checked("git", "remote", "set-url", "origin", remote_url)


def has_commit() -> bool:
    return run("git", "rev-parse", "--verify", "HEAD", check=False).returncode == 0


def sync_repository(default_branch: str) -> None:
    run_checked("git", "fetch", "--prune", "origin")
    remote_branch = run(
        "git",
        "ls-remote",
        "--exit-code",
        "--heads",
        "origin",
        default_branch,
        check=False,
    )
    if remote_branch.returncode != 0:
        print(f"Remote branch origin/{default_branch} does not exist; nothing to pull.")
        return

    run_checked(
        "git",
        "clean",
        "-fdx",
        "-e",
        ".devcontainer/github.local.yaml",
    )
    checkout = run(
        "git",
        "checkout",
        "-B",
        default_branch,
        "--force",
        f"origin/{default_branch}",
        check=False,
    )
    if checkout.returncode != 0:
        fail(
            f"cannot synchronize origin/{default_branch}: "
            f"{command_error(checkout)}"
        )
    run_checked("git", "branch", "--set-upstream-to", f"origin/{default_branch}", default_branch)


if not CONFIG_PATH.is_file():
    fail(
        f"configuration is missing: {CONFIG_PATH}. Copy "
        "github.local.yaml.example to github.local.yaml first."
    )

try:
    CONFIG_PATH.chmod(0o600)
    with CONFIG_PATH.open(encoding="utf-8") as config_stream:
        config = yaml.safe_load(config_stream)
except (OSError, yaml.YAMLError) as error:
    fail(f"unable to read {CONFIG_PATH}: {error}")

if not isinstance(config, dict):
    fail("the configuration must contain a YAML mapping")

github = config.get("github")
git = config.get("git", {})
if not isinstance(github, dict):
    fail("the github section is required")
if not isinstance(git, dict):
    fail("the git section must be a YAML mapping")

repository = github.get("repository")
token = github.get("token")
if not isinstance(repository, str) or not REPOSITORY_PATTERN.fullmatch(repository):
    fail("github.repository must be in OWNER/REPOSITORY form")
if token is not None and not isinstance(token, str):
    fail("github.token must be a string when provided")
if token is not None and (not token or token.endswith("REPLACE_ME")):
    token = None

default_branch = git.get("default_branch", "main")
if not isinstance(default_branch, str) or not BRANCH_PATTERN.fullmatch(default_branch):
    fail("git.default_branch contains invalid characters")

user_name = git.get("user_name")
user_email = git.get("user_email")
if user_name is not None and not isinstance(user_name, str):
    fail("git.user_name must be a string")
if user_email is not None and not isinstance(user_email, str):
    fail("git.user_email must be a string")

if not Path(".git").exists():
    run_checked("git", "init")

authenticate(repository, token)
configure_git(repository, user_name, user_email)
sync_repository(default_branch)
print(f"GitHub authentication and repository sync completed for {repository}.")
PY
