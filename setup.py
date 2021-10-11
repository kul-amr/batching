from setuptools import setup, find_packages

from codecs import open
from os import path

HERE = path.abspath(path.dirname(__file__))


with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="batching",
    version="0.1.0",
    description="Demo batching library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    author="Amruta K",
    author_email="",
    license="",
    packages=["batching"],
    include_package_data=True,
    install_requires=[],
    test_suite='tests',
    tests_require=[],
)