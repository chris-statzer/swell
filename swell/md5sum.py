import os
import logging

from swell.bash import bash_command
from swell.logger import get_logger

log = get_logger('MD5 ')


def md5sum(filename):
    log.info('Checking md5 of {}'.format(filename))
    md5_cmd = 'md5sum {}'.format(filename)
    md5 = os.popen(md5_cmd).read().split(' ')[0].rstrip()
    return md5
