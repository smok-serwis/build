Build repository for [smokserwis/build](https://hub.docker.com/r/smokserwis/build/)

This contains the  tool. Please read how it works
if you use [smokserwis/build](https://hub.docker.com/r/smokserwis/build/)+GitLab CI for 
building Docker images.

All tags can be found [here](dockerfiles).

## Additional commands

### Present in base

* `clean-apt-install` - update apt cache, install given packages with -y, clean up
* `clean-pip-install` - install given Python packages via pip, clean up

### Present in latest

* [docker-it](latest/README.md) - makes sense only with how we use GitLab CI for images.
* [check-syntax](latest/README.md) - verify that all JSON and YAML files are valid.
 
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

## jdk8

latest + JDK 8

## adk-cordova

jdk8 + Android toolkit + Cordova + NodeJS 5

## python9

Python 3.9 on x86_64 with Satella, Sphinx, Snakehouse and the wheel toolkit

## arm-python9

Python 3.9 on armv7l with Satella, Sphinx, Snakehouse and the wheel toolkit
