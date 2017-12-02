# Our specific build tools

## docker-it

`docker-it` is a Docker build wrapper script to be ran as part of CI environment.

Invoke this like:

```bash
docker-it myprojectname tagged_image_reference context_directory extra_args_for_docker_build
```
Image will be tagged with value of env `CI_COMMIT_REF_SLUG` of current build. If you are 
running this outside GitLab CI, please specify your own.


What it does is:
1. Alter target Dockerfile, by substituting `FROM` tag name with name of current branch.
   Define env ``DOCKERIT_NO_BRANCH`` to disable this behaviour. Target Dockerfile is taken 
2. Performs `docker build` 

* It assumes that current branch name is in `CI_COMMIT_REF_SLUG` env 

* Current branch name is 
It performs the common function of:

* Assuming branch name

* Build an image from given context and Dockerfile and tag it
* Substitute 
* Store entire SHA-1 reference to build image as target file

## check-jsons

It is an extra command to see if all (recursion will be applied) files ending
with .json are indeed valid JSON. 

It will return nonzero error code and point the culprit.
