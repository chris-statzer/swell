![LFS Logo](http://www.linuxfromscratch.org/images/lfs-logo.png)

This is a WIP build framework for the awesome Linux from Scratch project. The
goal is to provide an automated way to build the initial system and get a
working bootable disk. The host target is currently Ubuntu 16.04 LTS as a known
good host.

A further goal will be to use the built Python framework to also manage packages
for BLFS too.

Building

* Mount drive
* link $LFS/tools to /tools
* fix /bin/sh symlink `sudo update-alternatives --install /bin/sh sh /bin/bash 100`
* install build-essential, gawk, texinfo, bison, git
* install python packages pyyaml, docopt
* check versions with supplied script
* `./bin/swell build_temp_system

Additions

During the temp system install a few extras are needed to run the build system.
The list below are packages added to the temp systme built in chapter 5:

* temp-python-setuptools-33.1.1
* temp-python-docopt-0.6.2
* temp-python-pyyaml-3.12
* temp-pull-swell (pulls a copy of the framework into our env)

Current issues

* Test suite fails for temp diffutils-3.5 build when bootstrapping
* Build and test suite fails for temp file-5.29 util build when bootstrapping
  (zlib related) The only way I could fix this was to add a zlib build to the
  temp system. This seems to work fine and all the libs and bins have the
  correct signatures etc.
* Test suite fails for temp gawk-4.1.4 util build when bootstrapping
  (locale related)
* 2 tests in make fail had to disable (no idea)
* Error building Util-linux-2.29 with udev support. Had to disable in the
  configure opts.
* The optional bin strip currently does not work but is not an issue.
* Test suite for M4 currently fails with /checks/006.command_li:err
