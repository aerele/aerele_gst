# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in aerele_gst/__init__.py
from aerele_gst import __version__ as version

setup(
	name='aerele_gst',
	version=version,
	description='Frappe app to support GST requirements in manufacturing industries',
	author='Aerele Technologies Private Limited',
	author_email='hello@aerele.in',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
