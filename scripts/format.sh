#!/bin/sh -e
set -x

ruff check --fix --format pr_assistant tests docs scripts
