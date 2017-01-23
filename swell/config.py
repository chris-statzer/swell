import os
import logging

log = logging.getLogger('CONF')

ENV = {}

def setup_temp_build_env():
    log.info('Setting up temp system build env')
    ENV['LFS'] = '/mnt/lfs'
    ENV['LFS_TGT'] = 'x86_64-lfs-linux-gnu'
    ENV['LC_ALL'] = 'POSIX'
    ENV['PATH'] = '/tools/bin:' + os.environ['PATH']
    # log.info('Current PATH: \n\r{}'.format(os.environ['PATH']))

def setup_base_build_env():
    ENV['ZONEINFO'] = '/usr/share/zoneinfo'
    ENV['PATH'] = '/bin:/usr/bin:/sbin:/usr/sbin:/tools/bin'

# solve this programically
ROOT_PATH = os.getcwd()

CACHE_PATH = ROOT_PATH + '/cache'
SOURCE_PATH = ROOT_PATH + '/src'
PATCH_PATH = ROOT_PATH + '/patch'
BUILD_PATH = ROOT_PATH + '/build'
BACKUP_PATH = ROOT_PATH + '/backup'
DB_PATH = ROOT_PATH + '/db'
MAKE_OPTS = '-j 4'

ENV['CACHE_PATH'] = CACHE_PATH
ENV['SOURCE_PATH'] = SOURCE_PATH
ENV['PATCH_PATH'] = PATCH_PATH
ENV['BUILD_PATH'] = BUILD_PATH
ENV['MAKE_OPTS'] = MAKE_OPTS

# check paths and make them if needed
paths = [CACHE_PATH,
         SOURCE_PATH,
         PATCH_PATH,
         BUILD_PATH,
         DB_PATH,
         DB_PATH + '/installed',
         BACKUP_PATH]

for p in paths:
    if not os.path.isdir(p):
        log.info('Creating missing path: {}'.format(p))
        os.mkdir(p)
