import os
import subprocess
import logging

from swell import config

log = logging.getLogger('BASH')


def bash_command(cmd, env=config.ENV):
    # log.info('Running command: {} using ENV: {}'.format(cmd, env))
    proc = subprocess.Popen(['/bin/bash', '-c', '+h', cmd], env=env)
    return proc.wait()
