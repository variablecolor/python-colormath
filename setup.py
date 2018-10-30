#!/usr/bin/env python
# -*- coding: utf-8 -*-
import colormathfive

from setuptools import setup

LONG_DESCRIPTION = open('README.rst').read()

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Scientific/Engineering :: Mathematics',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
]

KEYWORDS = 'color math conversions'

setup(
    name='colormathfive',
    version=colormathfive.VERSION,
    description='Color math and conversion library.',
    long_description=LONG_DESCRIPTION,
    author='Gregory Taylor',
    author_email='gtaylor@gc-taylor.com',
    url='https://github.com/gtaylor/python-colormathfive',
    download_url='http://pypi.python.org/pypi/colormathfive/',
    packages=['colormathfive'],
    platforms=['Platform Independent'],
    license='BSD',
    classifiers=CLASSIFIERS,
    keywords=KEYWORDS,
    install_requires=['numpy', 'networkx>=2.0'],
)
