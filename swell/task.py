import logging
import os

from download import download
import config

log = logging.getLogger('TASK')

class Task(object):
    def __init__(self, package):
        super(Task, self).__init__()
        self.package = package

    def run(self):
        log.info('Running task: {}'.format(self.package.name))
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

        # Setup build path
        self.run_command('mkdir {}'.format(self.build_path))
        os.chdir(self.build_path)

        self.run_command_list(self.package.commands)

        # clean up and change the directory back to root
        os.chdir(config.ROOT_PATH)
        self.run_command('rm -rf {}'.format(self.build_path))


    def run_command(self, cmd):
        return_code = os.system(cmd)
        if return_code != 0:
            log.error('Nonzero return from command: {}'.format(cmd))
            exit()

    def run_command_list(self, cmd_list):
        for cmd in cmd_list:
            log.info('Running command: \n\r{}'.format(cmd))
            self.run_command(cmd)

    @property
    def build_path(self):
        return '{}/{}'.format(config.BUILD_PATH, self.package.name)
