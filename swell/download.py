import os
import logging

import config
import wget

log = logging.getLogger("DOWN")


def download(url, md5):
    #TODO: doesnt get md5sum of downloaded.....
    # log.info('downloading {} of type {}'.format(url, file_type))
    filename = url[url.rfind('/')+1:]
    if os.path.isfile('{}/{}'.format(config.CACHE_PATH, filename)):
        log.info('{} exists. Checking md5'.format(filename))
        cache_md5 = os.popen('md5sum {}/{}'.format(config.CACHE_PATH, filename)).read().split(' ')[0].rstrip()
        if cache_md5 == md5:
            log.info('Good md5 using the cached file.')
            return True
        else:
            log.error('File {} is bad!'.format(filename))
            exit()
    else:
        log.info('Fetching {}...'.format(url))
        wget.download(url)
        # return_code = os.system('wget -P {} {}'.format(config.CACHE_PATH, url))
        # if return_code != 0:
        #     log.error('Error downloading {}'.format(url))
        #     os.system('rm {}/{}'.format(config.CACHE_PATH, filename))
        #     exit()
        # else:
        #     return True
