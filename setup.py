#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Communications',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Message Boards',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
]

 
setup(
    name='cmsplugin-flickr-player',
    version='0.2.9.8',
    description='Flickr iframe with photo set for django-cms',
    author='ELCODO',
    author_email='info@elcodo.pl',
    url='https://github.com/elcodo/cmsplugin-flickr-player',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    license=open('LICENSE').read(),
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    long_description=open('README.md').read(),
)
