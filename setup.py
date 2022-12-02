#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name="envvar",
    version="0.0.1",
    description="Easiest way to deal with env vars",
    long_description=open("README.md", encoding="utf8").read(),
    author="Derich Pacheco",
    author_email="carlosderich@gmail.com",
    url="https://github.com/drish/envvar",
    packages=find_packages(exclude=["tests"]),
    package_data={"envvar": ["py.typed"]},
    install_requires=["pyyaml >= 6.0"],
    zip_safe=False,
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
