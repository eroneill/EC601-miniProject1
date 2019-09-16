#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="twiana",
    version="0.0.1",
    license="MIT",
    packages=find_packages(),
    setup_requires=["pytest-runner", "tweepy", "google-cloud-language"],
    test_requires=["pytest"],
    install_requires=["tweepy", "google-cloud-language"],
    python_requires=">=3.5",
)
