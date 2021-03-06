#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

PACKAGE = 'duedate'
VERSION = '0.0.2'

setup(
    name=PACKAGE,
    version=VERSION,
    description='Inherit due date for ticket from milestone due date',
    author="Tomas Pelka, Matej Cepl",
    license='GPL',
    url='https://github.com/tompelka/TracDueDate',
    packages=find_packages(exclude=['*.tests*']),
    entry_points = {'trac.plugins': ['duedate = duedate']},
    zip_safe = True
)
