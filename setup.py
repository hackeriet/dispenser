#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='dispenser',
      version='0.1.0',
      description='Dispenser software for Hackeriet',
      author='Hackeriet',
      author_email='karltk@hackeriet.no',
      url='http://hackeriet.no',
      install_requires=[],
      include_package_data = True,
      packages=find_packages(),
      entry_points = {
        'console_scripts': ['dispenser = hackeriet.tools.dispensertool:main'],
        'dispenser.build': ['default = dispenser']
        }
     )
