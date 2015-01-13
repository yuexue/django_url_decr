#!/usr/bin/env python

sdict = {
    'name': 'django_url_decr',
    'version': "0.1.0",
    'packages': ['django_url_decr'],
    'zip_safe': False,
    'install_requires': ['django'],
    'author': 'Lichun',
    'url': 'https://github.com/yuexue/django_url_decr',
    'classifiers': [
        'Environment :: Console',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python']
}

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(**sdict)
