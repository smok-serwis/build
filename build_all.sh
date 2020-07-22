#!/bin/bash
set -e

function build_for {
    docker build -t "smokserwis/build:$1-arm" $1
    docker push "smokserwis/build:$1-arm"
}

build_for base
build_for docker-only
build_for latest
