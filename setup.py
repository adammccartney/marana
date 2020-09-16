#!/usr/bin/env python
import setuptools


if __name__ == "__main__":
    setuptools.setup(
        author="Adam McCartney",
        author_email="adam@mur.at",
        install_requires=("abjad",),
        name="marana",
        packages=("marana",),
        url="https://github.com/adammccartney/marana",
        version="0.1",
        zip_safe=False,
    )
