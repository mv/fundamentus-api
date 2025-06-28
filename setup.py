
from setuptools import setup
from setuptools import find_packages


description='Fundamentus: API to load data from Fundamentus website: https://www.fundamentus.com.br/',

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='fundamentus',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},

    version='0.3.2',

#   scripts=[
#       'bin/fundamentus.csv.py',
#       'bin/magic_formula.simple.py',
#   ],

    url='https://github.com/mv/fundamentus-api/',
    author='Mv-Marcus Vinicius Ferreira',
    author_email='ferreira.mv@gmail.com',

    license='MIT',
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",

    install_requires=[
       'requests >= 2.32.4',
       'requests-cache >= 1.2.1',
       'pandas >= 2.3.0',
       'lxml >= 5.4.0',
       'tabulate >= 0.9.0',
    ],

    python_requires='>=3.9',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],


)
