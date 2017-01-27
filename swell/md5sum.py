import os
import logging

from swell.bash import bash_command

log = logging.getLogger('md5')


def md5sum(filename):
    log.info('Checking md5 of {}'.format(filename))
    md5_cmd = 'md5sum {}'.format(filename)
    md5 = os.popen(md5_cmd).read().split(' ')[0].rstrip()
    return md5
