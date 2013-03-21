#!/usr/bin/env python

from distutils.core import setup

setup(name='rtstool',
      version='0.1a2',
      description='rtslib command-line interface',
      author='Eric Harney',
      author_email='eharney@redhat.com',
      url='http://github.com/eharney/rtstool',
      scripts=['scripts/rtstool'],
      requires=['rtslib (>=2.1)'], # actually 2.1.fb27, but that is not a valid choice
      license='AGPLv3')
