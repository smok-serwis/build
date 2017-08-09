#!/usr/bin/python
# coding=UTF-8
from __future__ import print_function, absolute_import, division
import six
import logging
import os
import sys
import subprocess


DOCKERIT_NO_BRANCH = 'DOCKERIT_NO_BRANCH' in os.environ
DO_NOT_PUSH = 'DOCKERIT_DONT_PUSH' in os.environ
BRANCH_NAME = os.environ['CI_COMMIT_REF_SLUG']  # This env is required


def call(args, shell=False):
    rc = subprocess.call(args, shell=shell)
    if rc != 0:
        sys.exit(rc)


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

    if not DO_NOT_PUSH:
        call(['docker', 'push', TAG_BASED_REFERENCE])
        cmd = '''docker images --digests "'''+IMG_REFERENCE+''''" | grep '''+BRANCH_NAME+''' | awk '{ print $1"@"$3; }' | tail -1 > '''+PROJECT_NAME+'''.digest'''
        sys.stdout.write(cmd)
        rc = os.system(cmd)
        if rc != 0:
            sys.exit(rc)

        with open(PROJECT_NAME+'.digest', 'rb') as fin:
            sys.stdout.write('Uploaded as \n'+fin.read()+'\n'+TAG_BASED_REFERENCE+'\n')
