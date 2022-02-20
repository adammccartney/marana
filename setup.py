from setuptools import setup, find_packages

setup(
        name='marana',
        version='0.1.0',
        packages=find_packages(include=['marana', 'marana.*']),
        setup_requires=['pytest-runner'],
        tests_require=['pytest']
        )
