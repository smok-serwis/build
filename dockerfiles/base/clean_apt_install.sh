#!/bin/bash
set -e

mkdir -p /usr/share/man/man1/ /usr/share/man/man7/
apt-get update
apt-get install -y "$@"
apt-get clean
rm -rf /usr/share/man/*
