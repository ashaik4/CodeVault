from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# GUIDE: https://setuptools.readthedocs.io/en/latest/setuptools.html#developer-s-guide
setup(
    name='CodeVault',
    version='0.1.0',
    description='Repository containing Python Implementations of Various Algorithms and Datastructures',
    long_description=long_description,
    url='https://github.com/ashaik4/CodeVault',
    author='Arshad Shaik',
    author_email='arshadshaik992@gmail.com',
    license='MIT',
    keywords='prometheus',  # What does your project relate to?
    include_package_data=True,
    packages=find_packages(include=['*']),
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'pytest',
    ],

    # setup command line tool
    # entry_points={
    #     'console_scripts': [
    #         'tt-notifications-handler=notifications_handler.main:main'
    #     ]
    # }
)