import assert from "node:assert/strict";
import { existsSync, readFileSync } from "node:fs";
import test from "node:test";
import yaml from "js-yaml";

const workflowFile = (name) => new URL(`../.github/workflows/${name}.yml`, import.meta.url);
const workflow = (name) => yaml.load(readFileSync(workflowFile(name), "utf8"));
const deployCondition = "inputs.operation == 'deploy'";
const deleteCondition = "inputs.operation == 'delete'";

test("Pages workflows are separate, manual-only and serialize changes to the same site", () => {
  assert.equal(existsSync(workflowFile("deploy_gh")), false);
  for (const name of ["deploy_gh_pages", "deploy_gh_custom"]) {
    const config = workflow(name);
    assert.equal(config.name, name);
    assert.deepEqual(Object.keys(config.on), ["workflow_dispatch"]);
    const inputs = config.on.workflow_dispatch.inputs;
    assert.deepEqual(inputs.operation.options, ["deploy", "delete"]);
    assert.equal(inputs.operation.default, "deploy");
    assert.equal(inputs.operation.required, true);
    assert.equal(inputs.delete_confirmation.type, "string");
    assert.deepEqual(config.concurrency, { group: "github-pages", "cancel-in-progress": false });
    assert.deepEqual(config.permissions, { contents: "read" });
    assert.equal(config.jobs.pages.environment.name, "github-pages");
    assert.deepEqual(config.jobs.pages.permissions, {
      contents: "read", pages: "write", "id-token": "write",
    });
  }
});

test("each Pages workflow has an explicit domain mode with no custom-mode fallback", () => {
  const defaults = workflow("deploy_gh_pages");
  assert.equal(defaults.on.workflow_dispatch.inputs.custom_domain, undefined);
  const defaultConfigure = defaults.jobs.pages.steps.find((step) => step.id === "pages");
  assert.equal(defaultConfigure.run, "python3 -m scripts.github_pages configure-pages");
  assert.equal(defaultConfigure.env.CUSTOM_DOMAIN, undefined);
  assert.doesNotMatch(JSON.stringify(defaults), /PAGES_CUSTOM_DOMAIN|inputs\.custom_domain/);

  const custom = workflow("deploy_gh_custom");
  assert.equal(custom.on.workflow_dispatch.inputs.custom_domain.type, "string");
  assert.equal(custom.on.workflow_dispatch.inputs.custom_domain.required, false);
  const customConfigure = custom.jobs.pages.steps.find((step) => step.id === "pages");
  assert.equal(customConfigure.run, "python3 -m scripts.github_pages configure-custom");
  assert.equal(customConfigure.env.CUSTOM_DOMAIN, "${{ inputs.custom_domain || vars.PAGES_CUSTOM_DOMAIN }}");
});

test("both workflows build before configuration and separate confirmed deletion from deployment", () => {
  for (const name of ["deploy_gh_pages", "deploy_gh_custom"]) {
    const steps = workflow(name).jobs.pages.steps;
    const confirmation = steps.findIndex((step) => step.name === "Validate deletion confirmation");
    const build = steps.findIndex((step) => step.run === "npm ci && npm test");
    const configure = steps.findIndex((step) => step.id === "pages");
    const prepare = steps.findIndex((step) => step.run === "python3 -m scripts.prepare_site web");
    const upload = steps.findIndex((step) => step.uses?.startsWith("actions/upload-pages-artifact@"));
    const deploy = steps.findIndex((step) => step.id === "deployment");
    const deletion = steps.findIndex((step) => step.run === "python3 -m scripts.github_pages delete");
    assert.ok(confirmation >= 0 && confirmation < build && build < configure
      && configure < prepare && prepare < upload && upload < deploy && deploy < deletion);
    for (const index of [build, configure, prepare, upload, deploy]) {
      assert.equal(steps[index].if, deployCondition);
    }
    assert.equal(steps.find((step) => step.uses?.startsWith("actions/setup-node@")).if, deployCondition);
    for (const index of [confirmation, deletion]) {
      assert.equal(steps[index].if, deleteCondition);
      assert.equal(steps[index].env.DELETE_CONFIRMATION, "${{ inputs.delete_confirmation }}");
    }
    assert.match(steps[confirmation].run, /confirmation\(repository\(\)\)/);
    for (const index of [configure, deletion]) {
      assert.equal(steps[index].env.PAGES_ADMIN_TOKEN, "${{ secrets.PAGES_ADMIN_TOKEN }}");
    }
    assert.equal(steps[prepare].env.SITE_URL, "${{ steps.pages.outputs.site_url }}");
    assert.equal(steps[upload].with.path, "dist/web-site");
    assert.equal(steps[upload].with["include-hidden-files"], true);
    assert.equal(steps[0].with["persist-credentials"], false);
  }
});
