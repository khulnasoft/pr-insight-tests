#!/usr/bin/env bash

set -e
set -x

mypy pr_assistant
ruff check pr_assistant tests docs scripts
ruff format pr_assistant tests --check
