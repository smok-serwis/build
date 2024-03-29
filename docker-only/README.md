docker-it
=========

docker-it will additionally pass some build args:

- SAFE_BRANCH: either "develop" or "master", depending on which branch it is being built
  - develop if build on branch devel, development, develop or other
  - master if build on production, master or cloud
- BRANCH: name of the branch it's being built on 

Note that docker-it is prepared to cooperate with GitLab CI
Additionally, if you pass it --sub-wheels-requirements
then it will find a file called wheels_requirements.json
and replace every occurrence of "develop" with SAFE_BRANCH.

Also pass --postfix to postfix the result image with any tag

If you pass the -v flag, then both the command and resulting Dockerfile
will be printed.

strip-docs
==========

Note that strip-docs does "stupid strips", so if you use docstrings instead of a pass as a placeholder, you might
end up with stripped class looking like:

```python
class ImUsingDocstrings(AnotherClass):
```

Which is a `SyntaxError` in Python. So take care to put at least one pass or a ... in lieu of a placeholder.
