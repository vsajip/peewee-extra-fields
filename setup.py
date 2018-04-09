#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#
# To generate DEB package from Python Package:
# sudo pip3 install stdeb
# python3 setup.py --verbose --command-packages=stdeb.command bdist_deb
#
#
# To generate RPM package from Python Package:
# sudo apt-get install rpm
# python3 setup.py bdist_rpm --verbose --fix-python --binary-only
#
#
# To generate EXE MS Windows from Python Package (from MS Windows only):
# python3 setup.py bdist_wininst --verbose
#
#
# To generate PKGBUILD ArchLinux from Python Package (from PyPI only):
# sudo pip3 install git+https://github.com/bluepeppers/pip2arch.git
# pip2arch.py PackageNameHere
#
#
# To Upload to PyPI by executing:
# sudo pip install --upgrade pip setuptools wheel virtualenv
# python3 setup.py bdist_egg bdist_wheel --universal sdist --formats=zip upload --sign
#
# How to check if your modules are Cythonizable ?:
# cython -3 --verbose --no-docstrings your_module.py   # Pure Python,needs a *.pxd
# cython -3 --verbose --no-docstrings your_module.pyx  # Cython Syntax,dont need *.px
# gcc -O3 -march=native -shared -fPIC -I /usr/include/python3.6 -o your_module.so your_module.c


"""Setup.py for Python, as Generic as possible."""


import os
import re

from pathlib import Path

from setuptools import setup, Extension

try:
    from Cython.Build import cythonize
except ImportError:
    cythonize = None
    print(f"Cython not found, install Cython for Speed up: pip install cython")


from distutils.command import build as build_module


##############################################################################
# EDIT HERE


SOURCE = (Path(__file__).parent / "peewee_extra_fields" / "__init__.py").read_text()
MODULES2CYTHONIZE = ("peewee_extra_fields/ar_fields.py",
                     "peewee_extra_fields/us_fields.py",
                     "peewee_extra_fields/legacy_fields.py",
                     "peewee_extra_fields/regex_fields.py")


##############################################################################
# Dont touch below


class vuild(build_module.build):
  def run(self):
    # *.PY --> *.C
    cythons = cythonize(MODULES2CYTHONIZE, nthreads=9, exclude_failures=True, language_level=3)
    # *.C --> *.SO
    extensions = [
        Extension(str(Path(e).with_suffix("")).replace(os.sep, "."), s.sources, extra_compile_args=["-O3", "-finline-functions", "-shared"])
        for e, s in zip(MODULES2CYTHONIZE, cythons)]

    # Delete all *.C
    for c_files in cythons:
        for file2delete in c_files.sources:
            print(file2delete)
            # Path(file2delete).unlink()

    build_module.build.run(self)


setup(
    # cmdclass = {'build': vuild},
)
