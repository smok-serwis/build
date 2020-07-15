#!/usr/bin/python
# coding=UTF-8
from __future__ import print_function, absolute_import, division
import os
import sys
import subprocess
import re

DOCKERIT_NEW = 'DOCKERIT_NEW' in os.environ
DOCKERIT_NO_BRANCH = 'DOCKERIT_NO_BRANCH' in os.environ or DOCKERIT_NEW
DOCKERIT_NO_PUSH = 'DOCKERIT_NO_PUSH' in os.environ
DOCKERIT_NO_REQUIREMENTS = 'DOCKERIT_NO_REQUIREMENTS' in os.environ
DOCKERIT_CLASSIC_BRANCH = 'DOCKERIT_CLASSIC_BRANCH' in os.environ
BRANCH_NAME = os.environ['CI_COMMIT_REF_NAME']  # This env is required


from_line = re.compile(r'from (.*?):(.*?)( as .*)*')
requirements = re.compile(r'(.*?)git.dms-serwis.com.pl(.*?)@(develop)$')


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
    DOCKER_TAG_POSTFIX = ''

    if BRANCH_NAME == 'master':
        safe_branch = 'master'
    else:
        safe_branch = 'develop'

    if '-v' in extra_args_for_build:
        extra_args_for_build.remove('-v')
        VERBOSE = True
    else:
        VERBOSE = False

    if '--sub-wheels-requirements' in extra_args_for_build:
        extra_args_for_build.remove('--sub-wheels-requirements')
        with open('wheels_requirements.json', 'r') as f_in:
            data = f_in.read()
        data = data.replace('develop', safe_branch)
        with open('wheels_requirements.json', 'w') as f_out:
            f_out.write(data)

    extra_args_for_build.extend(['--build-arg',
                                 'BRANCH="%s"' % (BRANCH_NAME,),
                                 '--build-arg',
                                 'SAFE_BRANCH="%s"' % (safe_branch, )])

    TAG_BASED_REFERENCE = IMG_REFERENCE + ':' + BRANCH_NAME

    # Locate our Dockerfile!
    if '-f' not in extra_args_for_build:
        dockerfile_name = 'Dockerfile'
    else:
        f_index = extra_args_for_build.index('-f')
        dockerfile_name = extra_args_for_build[f_index+1]

    if '--postfix' in extra_args_for_build:
        i = extra_args_for_build.index('--postfix')
        DOCKER_TAG_POSTFIX = extra_args_for_build[i+1]
        extra_args_for_build.pop(i)
        extra_args_for_build.pop(i)

    if not DOCKERIT_NO_BRANCH:

        with open(dockerfile_name, 'rb') as fin_dockerfile:
            dockerfile = fin_dockerfile.read()

        linesep = b'\r\n' if b'\r\n' in dockerfile else b'\n'

        dockerfile_lines = dockerfile.split(linesep)

        if not DOCKERIT_CLASSIC_BRANCH:
            if BRANCH_NAME.lower() not in ('master', 'staging', 'develop'):
                BRANCH_NAME = 'develop'

        new_lines = []
        from_line_passed = False
        for line in dockerfile_lines:
            if line.lower().startswith('from') and not from_line_passed:
                elem = line.split(':')[-1]
                if 'as' in elem:
                    elem = elem.split('as')[0].strip()
                elif 'AS' in elem:
                    elem = elem.split('AS')[0].strip()

                from_line_passed = True

                sys.stdout.write('Altering Dockerfile %s tag %s -> %s\n' % \
                                 (dockerfile_name, elem, BRANCH_NAME+DOCKER_TAG_POSTFIX))

                line = line.replace(elem, BRANCH_NAME+DOCKER_TAG_POSTFIX)
            new_lines.append(line)

        dockerfile = linesep.join(new_lines)

        with open(dockerfile_name, 'wb') as fout_dockerfile:
            fout_dockerfile.write(dockerfile)

    if not DOCKERIT_NO_REQUIREMENTS:

        if not DOCKERIT_CLASSIC_BRANCH:
            if BRANCH_NAME.lower() not in ('master', 'staging', 'develop'):
                BRANCH_NAME = 'develop'

        req_file_name = os.path.join(CONTEXT_BUILD, 'requirements.txt')
        new_lines = []
        if os.path.exists(req_file_name):
            with open(req_file_name, 'r') as f_in:
                for line in f_in.readlines():
                    if requirements.match(line):
                        line = line.replace('develop', BRANCH_NAME)
                    new_lines.append(line)

            with open(req_file_name, 'w') as f_out:
                f_out.write('\n'.join(new_lines))

    call_args = ['docker', 'build', '-t', TAG_BASED_REFERENCE+DOCKER_TAG_POSTFIX] + \
                    extra_args_for_build + \
                    [CONTEXT_BUILD]
    if VERBOSE:
        with open(dockerfile_name, 'r') as f_in:
            print('Dockerfile is %s' % (f_in.read(), ))
        print('Calling %s' % (call_args, ))
    call(call_args)

    if not DOCKERIT_NO_PUSH:
        out = call(['docker', 'push', TAG_BASED_REFERENCE+DOCKER_TAG_POSTFIX], tap_stdout=True)
        print(out)
        ALLREF = IMG_REFERENCE + '@' + out.split(os.linesep)[-2].split(' ')[2]
        print(ALLREF)
        with open(PROJECT_NAME+'.digest', 'wb') as fout:
            fout.write(ALLREF)
        print('Written to', PROJECT_NAME+'.digest')
