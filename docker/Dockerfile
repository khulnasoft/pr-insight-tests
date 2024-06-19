FROM python:3.10 as base

WORKDIR /app
ADD pyproject.toml .
ADD requirements.txt .
RUN pip install . && rm pyproject.toml requirements.txt
ENV PYTHONPATH=/app

FROM base as github_app
ADD pr_assistant pr_assistant
CMD ["python", "-m", "gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-c", "pr_assistant/servers/gunicorn_config.py", "--forwarded-allow-ips", "*", "pr_assistant.servers.github_app:app"]

FROM base as bitbucket_app
ADD pr_assistant pr_assistant
CMD ["python", "pr_assistant/servers/bitbucket_app.py"]

FROM base as bitbucket_server_webhook
ADD pr_assistant pr_assistant
CMD ["python", "pr_assistant/servers/bitbucket_server_webhook.py"]

FROM base as github_polling
ADD pr_assistant pr_assistant
CMD ["python", "pr_assistant/servers/github_polling.py"]

FROM base as gitlab_webhook
ADD pr_assistant pr_assistant
CMD ["python", "pr_assistant/servers/gitlab_webhook.py"]

FROM base as azure_devops_webhook
ADD pr_assistant pr_assistant
CMD ["python", "pr_assistant/servers/azuredevops_server_webhook.py"]

FROM base as test
ADD requirements-dev.txt .
RUN pip install -r requirements-dev.txt && rm requirements-dev.txt
ADD pr_assistant pr_assistant
ADD tests tests

FROM base as cli
ADD pr_assistant pr_assistant
ENTRYPOINT ["python", "pr_assistant/cli.py"]
