import os
import subprocess
import sys

from swell import bash
from swell.download import download
from swell import config
from swell.logger import get_logger

log = get_logger('TASK')


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
            extract_cmd = 'tar xf {}/{} -C {}'.format(config.CACHE_PATH,
                                                      filename,
                                                      config.SOURCE_PATH)
            log.info('Extracting {} to {}'.format(filename,
                                                  config.SOURCE_PATH))
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
        self.run_command('touch {}/installed/{}'.format(config.DB_PATH,
                                                        self.package.name))

        # clean up and change the directory back to root
        os.chdir(config.ROOT_PATH)
        self.run_command('rm -rf {}'.format(self.build_path))

    def run_command(self, cmd):
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
