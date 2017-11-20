import os
from setuptools import setup, find_packages


if os.path.exists('README.rst'):
    long_description = open('README.rst').read()
else:
    long_description = '''Simple tool and library for downloading full albums from rajce.net'''

setup(
    name='rajce_downloader',
    version='1.0.0',
    author='Jiri Novotny',
    author_email='fg-42@seznam.cz',
    license='MIT',
    url='https://github.com/gorgitko/rajce-downloader-python',
    packages=find_packages(),
    description='Simple tool and library for downloading full albums from rajce.net',
    long_description=long_description,
    keywords='downloading rajce.net',
    zip_safe=False,
    entry_points={'console_scripts': ['rajce_downloader = rajce_downloader.cli:cli']},
    install_requires=['requests', 'beautifulsoup4'],
    classifiers=[],
)
