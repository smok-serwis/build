#!/usr/bin/python
# coding=UTF-8
from __future__ import print_function, absolute_import, division
import os
import json
import yaml
import sys

# First parameter is the directory to check
# Make sure, that all files that are JSON are indeed valid JSON
# used as a pre-build check


if __name__ == '__main__':
    for dirpath, dirnames, filenames in os.walk(u'.' if len(sys.argv) == 1 else sys.argv[1]):
        for filename in filenames:
            path = os.path.join(dirpath, filename)
            if filename.lower().endswith(u'.json'):
                with open(path, 'rb') as fin:
                    try:
                        json.load(fin)
                    except:
                        sys.stderr.write(u'Invalid JSON at '+path)
                        sys.exit(1)
            elif filename.lower().endswith(u'.yml') or filename.lower().endswith(u'.yaml'):
                with open(path, 'rb') as fin:
                    try:
                        yaml.load(fin)
                    except:
                        sys.stderr.write(u'Invalid JSON at '+path)
                        sys.exit(1)
