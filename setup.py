
from setuptools import setup
from setuptools import find_packages


description='Fundamentus: API to load data from Fundamentus website: https://www.fundamentus.com.br/',

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='fundamentus',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},

    version='0.1.0',

    scripts=[
        'bin/fundamentus.csv.py',
        'bin/magic_formula.simple.py',
    ],

    url='https://github.com/mv/fundamentus-api/',
    author='Mv-Marcus Vinicius Ferreira',
    author_email='ferreira.mv@gmail.com',

    license='MIT',
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",

    install_requires=[
       'requests >= 2.25.1',
       'requests-cache >= 0.5.2',
       'pandas >= 1.1.5',
       'lxml >= 4.6.2',
       'tabulate >= 0.8.7',
    ],

    python_requires='>=3.5',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],


)

