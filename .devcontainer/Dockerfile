FROM mcr.microsoft.com/devcontainers/base:ubuntu

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates \
        git \
        openssh-client \
        python3-yaml \
    && if ! id -u developer >/dev/null 2>&1; then \
        useradd --create-home --shell /bin/bash developer; \
    fi \
    && rm -rf /var/lib/apt/lists/*

USER developer
WORKDIR /workspace