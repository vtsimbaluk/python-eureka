# encoding: utf-8
from setuptools import setup, find_packages
from eureka import __version__ as version

import os


def here(fname):
    return os.path.join(os.path.dirname(__file__), fname)

setup(
    name='python-eureka',
    version=version,
    description='A python interface for Netflix Eureka',
    author=u'Kristian Øllegaard',
    author_email='kristian@oellegaard.com',
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(exclude=[]),
    install_requires=open(here('requirements.txt')).readlines(),
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ]
)