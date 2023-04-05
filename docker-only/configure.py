#!/usr/bin/python
# coding=UTF-8
"""

Accepts environment as target, ie:
    - [production|master|cloud|devel|develop|development|staging]
    else target environment will be staging

When called as such

    python configuration.py staging

It will rename all files containing ".staging." into "." and all files ending with .staging
with "". It will delete files and directories for the other environment.
Alternatively you can specify ".production." file name element to mark files which are
used on the production environment.

"""
from __future__ import print_function, absolute_import, division

import codecs
import json
import logging
import os.path
import shutil
import sys

logger = logging.getLogger(__name__)

if __name__ == '__main__':

    bad_endings = ['.production.', '.staging.', '.cloud.']
    if sys.argv[1] in ('master', 'production', 'cloud'):
        sys.argv[1] = 'production'
        good_ending = '.production.'
        print('*********** CONFIGURING FOR PRODUCTION ************')
    elif sys.argv[1] in ('devel', 'develop', 'staging', 'development'):
        print('******** CONFIGURING FOR STAGING INSTEAD **********')
        sys.argv[1] = 'staging'
        good_ending = '.staging.'
    elif sys.argv[1] == 'cloud':
        print('******** CONFIGURING FOR CLOUD INSTEAD **********')
        sys.argv[1] = 'cloud'
        good_ending = '.cloud.'
    bad_endings.remove(good_ending)

    good_ending_trim = good_ending[:-1]

    def process_good_ending(root_x, file_x, ending, replace_with):
        r_f = os.path.join(root_x, file_x)
        r_t = os.path.join(root_x, file_x.replace(ending, replace_with))
        logger.warning('Renaming %s to %s', r_f, r_t)
        os.rename(r_f, r_t)

    def process_bad_ending(root_x, file_x):
        path = os.path.join(root_x, file_x)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.unlink(path)

    for root, dirs, files in os.walk('.'):
        for file in files + dirs:
            if good_ending in file:
                process_good_ending(root, file, good_ending, '.')
            elif file.endswith(good_ending_trim):
                process_good_ending(root, file, good_ending_trim, '')
            else:
                for bad_ending in bad_endings:
                    if bad_ending in file:
                        process_bad_ending(root, file)
                    if file.endswith(bad_ending[:-1]):
                        process_bad_ending(root, file)

    if os.path.exists('server_list.txt'):
        servers = map(lambda q: q.strip(),
                      [q.decode('utf8') for q in open('server_list.txt', 'r').readlines() if
                       len(q.strip()) > 0])
    else:
        servers = []

    if os.path.exists('templates'):
        templates = dict((fn, open(os.path.join('templates', fn), 'rb').read()) for fn in
                         os.listdir('templates'))
    else:
        templates = {}

    for k in templates.keys()[:]:
        if k.endswith('.json'):
            v = templates.pop(k)
            templates.update(json.loads(v))

    for root, dirs, files in os.walk('.'):
        if '.git' in root:
            continue

        for file in files:
            altered = False

            file = os.path.join(root, file)
            try:
                with codecs.open(file, 'r', 'utf8') as fin:
                    lines = fin.readlines()
            except (IOError, UnicodeDecodeError):
                logger.error('Skipping %s' % (file,))
                continue

            newlines = []
            for line in lines:
                found = True
                while found:
                    found = False
                    for template in templates.keys():

                        assert template != 'SERVER'

                        templateF = '$%s$' % (template,)
                        if templateF in line:
                            altered = True
                            line = line.replace(templateF, templates[template])
                            found = True

                if '$SERVER$' in line:
                    newlines.extend([line.replace('$SERVER$', server) for server in servers])
                else:
                    newlines.append(line)
            if altered:
                with codecs.open(file, 'w', 'utf8') as f_out:
                    logger.warning('Adjusting %s', file)
                    f_out.writelines(newlines)
