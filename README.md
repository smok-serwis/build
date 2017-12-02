Build repository for [smokserwis/build](https://hub.docker.com/r/smokserwis/build/)

This contains the [docker-it](latest/build_tools/README.md) tool. Please read how it works
if you use [smokserwis/build](https://hub.docker.com/r/smokserwis/build/)+GitLab CI for 
building Docker images.

All tags can be found [here](dockerfiles).

## Additional commands

* `clean-apt-install` - update apt cache, install given packages with -y, clean up
* `clean-pip-install` - install given Python packages via pip, clean up

# Tags
## base

Basic Linux utilities and pip-ready Python 2.7

## latex

base + latex + pandoc

## docker-only

base + has Docker and docker-compose

## latest

docker-only + usual build tools

## node7

latest + typical NodeJS 7 utils for websites

## adk-cordova

latest + Android toolkit + Cordova + NodeJS 5