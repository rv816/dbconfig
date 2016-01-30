import setuptools

setuptools.setup(
    name="dbconfig",
    version="0.1.0",
    url="https://github.com/borntyping/cookiecutter-pypackage-minimal",

    author="Ryan Vass",
    author_email="rvsax16@gmail.com",

    description="Pip installable dbconfig",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[
        'dataset'],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
