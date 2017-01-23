import logging
import os
import subprocess
import sys

import bash
from download import download
import config

log = logging.getLogger('TASK')

class Task(object):
    def __init__(self, package):
        super(Task, self).__init__()
        self.package = package

    def run(self):
        log.info('Running task: {}'.format(self.package.name))
        sys.stdout.write("\033]0;TASK({})\007".format(self.package.name))
        sys.stdout.flush()

        # Check if installed
        if os.path.isfile('{}/installed/{}'.format(config.DB_PATH,
                                                   self.package.name)):
            log.info('{} is already installed skipping!'.format(
                self.package.name))
            return True

        # Download archives
        if self.package.src_uri:
            download(self.package.src_uri, self.package.md5)

            # extract the package to the src directory
            url = self.package.src_uri
            filename = url[url.rfind('/')+1:]
            tar_flags = ''
            if url[-2:] == 'gz':
                tar_flags = 'xzf'
            elif url[-2:] == 'xz':
                tar_flags = 'xJf'
            elif url[-3:] == 'bz2':
                tar_flags = 'xjf'
            extract_cmd = 'tar {} {}/{} -C {}'.format(tar_flags, config.CACHE_PATH, filename, config.SOURCE_PATH)
            log.info('Extracting {} to {}'.format(filename, config.SOURCE_PATH))
            self.run_command(extract_cmd)

        # delete old build directory if it exists
        if os.path.isdir(self.build_path):
            self.run_command('rm -rf {}'.format(self.build_path))

        # Setup build path
        os.mkdir(self.build_path)
        os.chdir(self.build_path)

        self.run_command_list(self.package.commands)

        log.info('{} installed successfully,'.format(self.package.name))

        # mark package as installed
        log.info('Marking {} as installed...'.format(self.package.name))
        self.run_command('touch {}/installed/{}'.format(config.DB_PATH, self.package.name))

        # clean up and change the directory back to root
        os.chdir(config.ROOT_PATH)
        self.run_command('rm -rf {}'.format(self.build_path))


    def run_command(self, cmd):
        log.info('Running command: \n\r{}'.format(cmd))
        return_code = bash.bash_command(cmd)
        if return_code != 0:
            log.error('Nonzero return from command: {}'.format(cmd))
            exit()

    def run_command_list(self, cmd_list):
        for cmd in cmd_list:
            self.run_command(cmd)

    @property
    def build_path(self):
        return '{}/{}'.format(config.BUILD_PATH, self.package.name)
