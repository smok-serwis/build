#!/bin/bash
set -e

docker buildx create --name builder
docker buildx use builder
docker buildx inspect --bootstrap

function build_for {
    docker buildx build --push -t "smokserwis/build:$1" $1
}

build_for base
build_for latex
build_for docker-only
build_for latest
build_for jdk8
build_for adk-cordova
build_for node7
build_for node10
build_for python9
docker buildx build -t smokserwis/build:arm-python3  --platform linux/arm/v7 --progress plain arm-python3
docker buildx build -t smokserwis/build:arm-python9  --platform linux/arm/v7 --progress plain arm-python9
docker buildx build -t smokserwis/build:aarch64  --platform linux/arm64 --progress plain aarch64
docker buildx use default
docker buildx rm builder
