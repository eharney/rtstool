#!/usr/bin/env python

# Copyright 2013 Red Hat, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, version 3 (AGPLv3).
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


from distutils.core import setup

setup(name='rtstool',
      version='0.1a3',
      description='rtslib command-line interface',
      author='Eric Harney',
      author_email='eharney@redhat.com',
      url='http://github.com/eharney/rtstool',
      scripts=['scripts/rtstool'],
      requires=['rtslib (>=2.1)'], # actually 2.1.fb27, but that is not a valid choice
      license='AGPLv3')
