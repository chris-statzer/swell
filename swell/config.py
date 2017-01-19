import os
import logging

log = logging.getLogger('CONF')


def setup_temp_build_env():
    log.info('Setting up temp system build env')
    if not 'LFS' in os.environ:
        os.environ['LFS'] = '/mnt/lfs'

    if not 'LFS_TGT' in os.environ:
        os.environ['LFS_TGT'] = 'x86_64-lfs-linux-gnu'

    os.environ['LC_ALL'] = 'POSIX'


    os.environ['PATH'] = '/tools/bin:' + os.environ['PATH']
    # log.info('Current PATH: \n\r{}'.format(os.environ['PATH']))

def setup_base_build_env():
    os.environ['ZONEINFO'] = '/usr/share/zoneinfo'
    os.environ['PATH'] = '/bin:/usr/bin:/sbin:/usr/sbin:/tools/bin'

# solve this programically
ROOT_PATH = os.getcwd()

CACHE_PATH = ROOT_PATH + '/cache'
SOURCE_PATH = ROOT_PATH + '/src'
PATCH_PATH = ROOT_PATH + '/patch'
BUILD_PATH = ROOT_PATH + '/build'
BACKUP_PATH = ROOT_PATH + '/backup'
DB_PATH = ROOT_PATH + '/db'
MAKE_OPTS = '-j 4'

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
