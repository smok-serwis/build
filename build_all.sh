#!/bin/bash
set -e

function build_for {
    cd $1
    docker build -t "smokserwis/build:$1" .
    docker push "smokserwis/build:$1"
    cd ..
}

build_for base
build_for latex
build_for docker-only
build_for latest
build_for adk-cordova
build_for node7
