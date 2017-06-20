# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

setup(
    name='word-guess',
    version='0.1.0',
    description='Package for word guessing game',
    long_description=readme,
    author='Sander Lepik',
    author_email='sander.lepik@knowit.ee',
    url='https://github.com/sanderlepik/word-guess',
    packages=['wordgame'],
    entry_points={
        'setuptools.installation': [
            'eggsecutable = wordgame.core:word_game',
        ]
    },
    scripts=['word-guess-executable'],
)


