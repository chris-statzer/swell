import os
import logging

from swell.download import download
from sell.config import CACHE_PATH

log = logging.getLogger('INIT')


if os.system('which pip3') != 0:
    log.error('Pip not found, fetching!')
    download('https://bootstrap.pypa.io/get-pip.py')
    os.system('wget  && python3 get-pip.py')

try:
    import docopt
except ImportError:
    log.error('docopt not found, installing')
    os.system('pip3 install docopt')

try:
    import yaml
except ImportError:
    os.system('pip3 install pyyaml')
