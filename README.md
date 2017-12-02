Build repository for [smokserwis/build](https://hub.docker.com/r/smokserwis/build/)

This contains the [docker-it](dockerfiles/latest/build_tools/README.md) tool. Please read how it works
if you use [smokserwis/build](https://hub.docker.com/r/smokserwis/build/)+GitLab CI for 
building Docker images.

All tags can be found [here](dockerfiles).

## Additional commands

* `clean-apt-install` - update apt cache, install given packages with -y, clean up
* `clean-pip-install` - install given Python packages via pip, clean up
