#!/bin/bash
set -e

function build_for {
    docker build -t "smokserwis/build:$1" $1
    docker push "smokserwis/build:$1"
}

build_for base
build_for latex
build_for docker-only
build_for latest
build_for adk-cordova
build_for node7
