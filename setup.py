#!/usr/bin/env python

"""The setup script."""
from setuptools import setup, find_packages

# meta:
meta = {"__author__": "Yi Q",
        "__email__": "yitistica@outlook.com",
        "__version__": "1.0.5"}


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
            'Programming Language :: Python :: 3.11',
            'Programming Language :: Python :: 3.12'
        ],
        description="a package that handles months.",
        install_requires=requirements,
        license="MIT license",
        long_description=readme + '\n\n' + history,
        long_description_content_type='text/x-rst',
        include_package_data=True,
        keywords='month, date',
        name='datetime-month',
        packages=find_packages(where='src'),
        package_dir={'': 'src'},
        setup_requires=setup_requirements,
        test_suite='tests',
        tests_require=test_requirements,
        url='https://github.com/yitistica/month',
        version=meta['__version__'],
        zip_safe=False,
    )
