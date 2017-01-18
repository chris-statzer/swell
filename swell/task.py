import logging
import os

import download

log = logging.getLogger('TASK')

class Task(object):
    def __init__(self, package):
        super(Task, self).__init__()
        self.package = package

    def run(self):
        log.info('Running task: {}'.format(self.package.name))


    def run_command(self, cmd):
        return_code = os.system(cmd)
        if return_code != 0:
            log.error('Nonzero return from command: {}'.format(cmd))
            exit()

    def run_command_list(self, cmd_list):
        for cmd in cmd_list:
            log.info('Running command: \n\r{}'.format(cmd))
            self.run_command(cmd)
