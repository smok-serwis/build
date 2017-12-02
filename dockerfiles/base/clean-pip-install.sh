#!/bin/bash
set -e
pip install "$@"
rm -rf /root/.cache /tmp/pip-*
