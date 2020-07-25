#!/bin/bash
set -e
pip3 install "$@"
rm -rf /root/.cache /tmp/pip-*
