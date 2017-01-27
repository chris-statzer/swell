import os
import subprocess
import logging

from swell import config
from swell.logger import get_logger
log = get_logger('BASH')


def bash_command(cmd, env=config.ENV):
    # log.info('Running command: {} using ENV: {}'.format(cmd, env))
    log.info('Running command: \n\r\t - {}'.format(cmd))
    proc = subprocess.Popen(['/bin/bash', '-c', '+h', cmd], env=env)
    return proc.wait()
