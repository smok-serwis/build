#!/usr/bin/python
# coding=UTF-8
from __future__ import print_function, absolute_import, division
import six
import logging
import os
import sys
import subprocess
import tempfile


DOCKERIT_NO_BRANCH = 'DOCKERIT_NO_BRANCH' in os.environ
DOCKERIT_NO_PUSH = 'DOCKERIT_NO_PUSH' in os.environ
BRANCH_NAME = os.environ['CI_COMMIT_REF_SLUG']  # This env is required


def call(args, shell=False, tap_stdout=False):

    stdout = None

    if tap_stdout:
        x = open('stdout', 'a+')
        x.seek(0, 0)
        stdout = x.fileno()

    rc = subprocess.call(args, shell=shell, stdout=stdout)

    if tap_stdout:
        x.seek(0, 0)
        stdout = x.read()
        x.close()
    else:
        stdout = ''

    if rc != 0:
        sys.exit(rc)

    return stdout


if __name__ == '__main__':

    PROJECT_NAME, IMG_REFERENCE, CONTEXT_BUILD = sys.argv[1:4]
    extra_args_for_build = sys.argv[4:]

    TAG_BASED_REFERENCE = IMG_REFERENCE + ':' + BRANCH_NAME

    # Locate our Dockerfile!
    if '-f' not in extra_args_for_build:
        dockerfile_name = 'Dockerfile'
    else:
        f_index = extra_args_for_build.index('-f')
        dockerfile_name = extra_args_for_build[f_index+1]

    if not DOCKERIT_NO_BRANCH:

        with open(dockerfile_name, 'rb') as fin_dockerfile:
            dockerfile = fin_dockerfile.read()

        linesep = b'\r\n' if b'\r\n' in dockerfile else b'\n'

        dockerfile_lines = dockerfile.split(linesep)

        if not dockerfile_lines[0].startswith('FROM'):
            sys.stderr.write('''First line of Dockerfile does not start with FROM.
It starts with '+dockerfile_lines[0]+' instead''')
            sys.exit(1)

        elements = dockerfile_lines[0].split(':')

        sys.stdout.write('Altering Dockerfile %s tag %s -> %s' % \
                         (dockerfile_name, elements[-1], BRANCH_NAME))

        dockerfile_lines[0] = dockerfile_lines[0].replace(elements[-1], BRANCH_NAME)
        dockerfile = linesep.join(dockerfile_lines)

        with open(dockerfile_name, 'wb') as fout_dockerfile:
            fout_dockerfile.write(dockerfile)
        #debug
        sys.stdout.write(dockerfile)

    call(['docker', 'build', '-t', TAG_BASED_REFERENCE] + \
                    extra_args_for_build + \
                    [CONTEXT_BUILD])

    if not DOCKERIT_NO_PUSH:
        out = call(['docker', 'push', TAG_BASED_REFERENCE], tap_stdout=True)
        print(out)
        ALLREF = IMG_REFERENCE + '@' + out.split(os.linesep)[-2].split(' ')[2]
        print(ALLREF)
        with open(PROJECT_NAME+'.digest', 'wb') as fout:
            fout.write(ALLREF)
        print('Written to', PROJECT_NAME+'.digest')
