import os
import logging

from swell import config

log = logging.getLogger("DOWN")


def download(url, md5=None):
    """ TODO: doesnt get md5sum of downloaded.....
        log.info('downloading {} of type {}'.format(url, file_type)) """
    filename = url[url.rfind('/')+1:]
    if os.path.isfile('{}/{}'.format(config.CACHE_PATH, filename)):
        if md5 is None:
            return True
        log.info('{} exists. Checking md5'.format(filename))
        md5_cmd = 'md5sum {}/{}'.format(config.CACHE_PATH, filename)
        cache_md5 = os.popen().read().split(md5_cmd)[0].rstrip()
        if cache_md5 == md5:
            log.info('Good md5 using the cached file.')
            return True
        else:
            log.error('File {} is bad!'.format(filename))
            exit()
    else:
        log.info('Fetching {}...'.format(url))
        # wget.download(url)
        return_code = os.system('wget -P {} {}'.format(config.CACHE_PATH, url))
        if return_code != 0:
            log.error('Error downloading {}'.format(url))
            os.system('rm {}/{}'.format(config.CACHE_PATH, filename))
            exit()
        else:
            return True
