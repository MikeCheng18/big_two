#!/usr/bin/env python

from setuptools import setup, find_packages

with open("requirements.txt") as f:
	requirements = f.read().splitlines()

setup(
    name="bigtwo",
    version="0.1.23",
    packages=find_packages(include=["bigtwo", "bigtwo.*"]),
    description="Python tutorial",
    author="Mike",
    author_email="mikecheng2001@gmail.com",
    url="http://youtube.com/",
    install_requires=requirements
)
