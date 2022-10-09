#!/usr/bin/env python

"""The setup script."""

from pathlib import Path
import json
from setuptools import setup, find_packages

# meta:
meta_file_name = 'src/month/meta.json'
meta_path = Path(__file__).resolve().parent.joinpath(meta_file_name)


try:
    with open(meta_path) as file:
        meta = json.load(file)
    del file
except FileNotFoundError:
    meta = dict()


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = []

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]


if __name__ == '__main__':
    setup(
        author=meta.get('__author__', ''),
        author_email=meta.get('__email__', ''),
        python_requires='>=3.6',
        classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Natural Language :: English',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
        ],
        description="a package that handles months.",
        install_requires=requirements,
        license="MIT license",
        long_description=readme + '\n\n' + history,
        include_package_data=True,
        keywords='month, date',
        name='datetime-month',
        packages=find_packages(where='src'),
        package_dir={'': 'src'},
        setup_requires=setup_requirements,
        test_suite='tests',
        tests_require=test_requirements,
        url='https://github.com/yitistica/month',
        version=meta.get('__version__', '0.1.0'),
        zip_safe=False,
    )
