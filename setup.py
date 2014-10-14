
from distutils.core import setup
setup(
    name = "colino",
    packages = ["colino"],
    version = "0.0.1",
    description = "Event correlator",
    author = "Gabriele Mambrini",
    author_email = "g.mambrini@gmail.com"
    url = "http://github.com/gmambro/colino",
#    download_url = "",
    keywords = ["event" ],
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
    long_description = """\
Colino simple event correlator
"""
)
