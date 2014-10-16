from setuptools import setup, find_packages # Always prefer setuptools over distutils
from codecs import open # To use a consistent encoding
from os import path
here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = "colino",
    version = "0.0.1",
    
    description = "Event correlator",
    long_description = long_description,

    author = "Gabriele Mambrini",
    author_email = "g.mambrini@gmail.com",

    url = "http://github.com/gmambro/colino",
    # download_url = "",

    classifiers = [
        "Programming Language :: Python",

	# 3 - Alpha
	# 4 - Beta
	# 5 - Production/Stable
        "Development Status :: 3 - Alpha",

        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",

	'Programming Language :: Python :: 2',
	'Programming Language :: Python :: 2.6',
	'Programming Language :: Python :: 2.7',

        ],
    license = 'Apache',

    keywords = ["event" ],

    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    entry_points={
        'console_scripts': [
             'colino=colino:main',
        ],
    },
)
