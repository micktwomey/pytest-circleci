import textwrap

from setuptools import setup

from pytest_circleci import __version__
from pytest_circleci import plugin

setup(
    name="pytest-circleci",
    version=__version__,
    description="py.test plugin for CircleCI",
    long_description=textwrap.dedent(plugin.pytest_collection_modifyitems.__doc__),
    author="Michael Twomey",
    author_email="mick@twomeylee.name",
    url="https://github.com/micktwomey/pytest-circleci",
    packages=["pytest_circleci"],
    entry_points={
        'pytest11': [
            'circleci = pytest_circleci.plugin'
        ],
    },
    classifiers=(
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        # "Programming Language :: Python :: 3",  Not tested yet
    ),
)
