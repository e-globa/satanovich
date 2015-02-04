#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path
from setuptools import setup

FOLDER = path.dirname(__file__)


def get_requirements():
    requirements_file = path.join(FOLDER, 'requirements.txt')
    with open(requirements_file) as f:
        return f.read().splitlines()


setup(
    name='satanovich',
    version='0.1',
    author='Satanovskyj Dmytro',
    author_email='satandmytro@gmail.com',
    install_requires=get_requirements(),
    entry_points={
        'console_scripts': [
            'runserver = runserver:run',
        ],
    }
)
