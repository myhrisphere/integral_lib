from setuptools import setup, find_packages

setup(
    name='integral_lib',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.21.0',
        'sympy>=1.10.0'
    ],
    description='Library for calculating integrals',
    author='myhrisphere',
    license='MIT'
)
