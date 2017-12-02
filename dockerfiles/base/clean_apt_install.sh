#!/bin/bash
set -e

apt-get update
apt-get install -y "$@"
apt-get clean
rm -rf /usr/share/man/*
