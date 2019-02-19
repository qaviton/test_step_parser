#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


""" updating pip version:
    ---------------------

1) increase test_step_parser.version.__version__

2) make sure these are installed:
    pip install wheel
    python setup.py bdist_wheel --universal
    pip install twine

3) run these:
    python setup.py sdist
    python setup.py bdist_wheel
    twine upload dist/*
"""


import io
from test_step_parser import __version__ as version
from setuptools import setup, find_packages


packages = []
for package in find_packages():
    if package.startswith('test_step_parser'):
        packages.append(package)


with io.open('README.rst', 'rt', encoding='utf8') as f:
    readme = f.read()


setup(
    name='test_step_parser',
    version=version,
    description='The test step parser is a universal format for '
                'describing automated test steps & automatically'
                ' parse source code and generate a step metadata'
                ' for AI & humans to create automated tests fast'
                ' and easy.',
    long_description=readme,
    keywords=['test_step_parser'],
    author='Yehonadav Bar Elan',
    author_email='yehonadav@Qaviton.com',
    url='https://qaviton.com/',
    packages=packages,
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Environment :: Console',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
    ],
    install_requires=[]
)
