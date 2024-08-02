#!/bin/sh -e
set -x

ruff check pr_assistant tests docs scripts --fix
ruff format pr_assistant tests docs scripts
