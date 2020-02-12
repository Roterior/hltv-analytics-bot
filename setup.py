#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


def parse_requirements(filename):
    line_iter = (line.strip() for line in open(filename))
    return [line for line in line_iter if line and not line.startswith("#")]


packages = parse_requirements('./requirements.txt')
print(packages)

setup(
    name='hltvAnalyticsBot',
    version='0.1',
    packages=['src'],
    install_requires=packages,
    url='',
    license='',
    author='Alex If',
    author_email='roterior@gmail.com',
    description='analytics bot'
)
