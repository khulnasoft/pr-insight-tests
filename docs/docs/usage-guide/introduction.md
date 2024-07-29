
After [installation](https://pr-assistant-docs.khulnasoft.com/installation/), there are three basic ways to invoke KhulnaSoft PR-Assistant:

1. Locally running a CLI command
2. Online usage - by [commenting](https://github.com/Khulnasoft/pr-assistant/pull/229#issuecomment-1695021901) on a PR
3. Enabling PR-Assistant tools to run automatically when a new PR is opened


Specifically, CLI commands can be issued by invoking a pre-built [docker image](https://pr-assistant-docs.khulnasoft.com/installation/locally/#using-docker-image), or by invoking a [locally cloned repo](https://pr-assistant-docs.khulnasoft.com/installation/locally/#run-from-source).

For online usage, you will need to setup either a [GitHub App](https://pr-assistant-docs.khulnasoft.com/installation/github/#run-as-a-github-app) or a [GitHub Action](https://pr-assistant-docs.khulnasoft.com/installation/github/#run-as-a-github-action) (GitHub), a [GitLab webhook](https://pr-assistant-docs.khulnasoft.com/installation/gitlab/#run-a-gitlab-webhook-server) (GitLab), or a [BitBucket App](https://pr-assistant-docs.khulnasoft.com/installation/bitbucket/#run-using-khulnasoft-hosted-bitbucket-app) (BitBucket).
These platforms also enable to run PR-Assistant specific tools automatically when a new PR is opened, or on each push to a branch.

