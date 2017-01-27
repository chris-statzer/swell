
from glob import glob
import logging

import yaml

log = logging.getLogger('PACK')


class Package(object):
    """docstring for Package."""
    def __init__(self, filename):
        super(Package, self).__init__()
        with open(filename, 'r') as package_file:
            log.info('Loading {}'.format(filename))
            self.data = yaml.load(package_file.read())

    @property
    def name(self):
        return self.data['name']

    @property
    def version(self):
        return self.data['version']

    @property
    def description(self):
        return self.data.get('description', '(none)')

    @property
    def deps(self):
        return self.data.get('deps', [])

    @property
    def src_uri(self):
        return self.data.get('src_uri', None)

    @property
    def md5(self):
        return self.data.get('md5', None)

    @property
    def patch(self):
        return self.data.get('patch', [])

    @property
    def homepage(self):
        return self.data.get('homepage', '(none)')

    @property
    def commands(self):
        return self.data.get('commands', [])


def load_packages():
    package_glob = glob('./packages/*.yaml')

    packages = {}
    for p in package_glob:
        # log.info('Loading package: {}'.format(p))
        package = Package(p)
        packages[package.name] = package
    return packages


def _resolve(package_list, package):
    dep_list = []
    if package in package_list:
        for dep in package_list[package].deps:
            if package_list[dep].deps:
                dep_list += _resolve(package_list, dep)
            dep_list.append(dep)
    return dep_list


def _flatten(package_list):
    packages = []
    for p in package_list:
        if p not in packages:
            packages.append(p)
    return packages


def resolve_deps(package):
    package_list = load_packages()
    deps_list = [package, ]
    deps_list += _resolve(package_list, package)
    deps_list = _flatten(deps_list)
    return deps_list


def dump_packages():
    package_list = load_packages()
    print('Package list:\n\r')
    for k, v in package_list.items():
        print('       Name:', v.name, v.version)
        print('Description:', v.description)
        if v.deps:
            print('       Deps:')
            for d in v.deps:
                print('          - ', d)
        print('')
