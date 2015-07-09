import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = "sprint_tutorial",
    version = "0.0.1",
    author = "Jonathan Rocher",
    author_email = "jonathanrocher@gmail.com",
    description = ("Sample repository to learn to sprint on open source "
                   "software"),
    license = "BSD",
    keywords = "example sprint tutorial",
    url = "https://github.com/jonathanrocher/sprint_tutorial",
    packages=['sprint_tutorial'],
    long_description=read('README.md'),
    classifiers=[
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
