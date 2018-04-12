#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

VERSION_RE = re.compile(r'(\d+\.\d+\.\d+)')

with open('CHANGES.txt') as changelog:
    CHANGES = changelog.read()
    first_line = changelog.readline()
    match = VERSION_RE.search(first_line)
    if not match:
        raise RuntimeError('Could not determine a valid version from changelog.')

    version = match.group(1)

requires = [
    'plaster_pastedeploy',
    'pyramid',
    'pyramid_jinja2',
    'pyramid_debugtoolbar',
    'waitress',
]

tests_require = [
    'WebTest >= 1.3.1',
    'pytest',
    'pytest-cov',
]

setup(
    name='api_pyramid_quote',
    version=version,
    description='api_pyramid_quote',
    long_description=README + "\n\n" + CHANGES,
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='Rocky Shimithy',
    author_email='shimithy@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': tests_require,
    },
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = api_pyramid_quote:main',
        ],
    },

)
