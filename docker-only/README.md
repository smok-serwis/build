docker-it will additionally pass some build args:

- SAFE_BRANCH: either "develop" or "master", depending on which branch it is being built
- BRANCH: name of the branch it's being built on 

Note that docker-it is prepared to cooperate with GitLab CI
Additionally, if you pass it --sub-wheels-requirements
then it will find a file called wheels_requirements.json
and replace every occurrence of "develop" with SAFE_BRANCH.

If you pass the -v flag, then both the command and resulting Dockerfile
will be printed.

There's an additional command available, called strip-docs.
Given a target directory it will find all .pyx, .py and .pyd files
and strip them of comments and docstrings. Use it like this:

```bash
strip-docs .
```
