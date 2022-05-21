from setuptools import setup, find_packages

VERSION = '1.0'

setup(
    name='fracdiff',
    version=VERSION,
    description='Fractional Differentiation framework for time series.',
    author='Arnab Bhowmik',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
    ]
)
