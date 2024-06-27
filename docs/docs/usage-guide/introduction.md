
After [installation](https://khulnasoft.github.io/installation/), there are three basic ways to invoke KhulnaSoft PR-Assistant:

1. Locally running a CLI command
2. Online usage - by [commenting](https://github.com/khulnasoft/pr-assistant/pull/229#issuecomment-1695021901) on a PR
3. Enabling PR-Assistant tools to run automatically when a new PR is opened


Specifically, CLI commands can be issued by invoking a pre-built [docker image](https://khulnasoft.github.io/installation/locally/#using-docker-image), or by invoking a [locally cloned repo](https://khulnasoft.github.io/installation/locally/#run-from-source).
For online usage, you will need to setup either a [GitHub App](https://khulnasoft.github.io/installation/github/#run-as-a-github-app), or a [GitHub Action](https://khulnasoft.github.io/installation/github/#run-as-a-github-action).
GitHub App and GitHub Action also enable to run PR-Assistant specific tool automatically when a new PR is opened.


**git provider**: The [git_provider](https://github.com/khulnasoft/pr-assistant/blob/main/pr_assistant/settings/configuration.toml#L5) field in the configuration file determines the GIT provider that will be used by PR-Assistant. Currently, the following providers are supported:
`
"github", "gitlab", "bitbucket", "azure", "codecommit", "local", "gerrit"
`

