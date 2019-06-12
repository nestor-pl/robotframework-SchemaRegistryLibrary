#!/usr/bin/env python

from os.path import join, dirname
from setuptools import setup

filename=join(dirname(__file__), 'SchemaRegistryLibrary', 'version.py')
exec(compile(open(filename).read(),filename, 'exec'))

DESCRIPTION = """
Schema Registry library for Robot Framework.
"""[1:-1]

setup(name         = 'robotframework-schemaregistrylibrary',
      version      = VERSION,
      description  = 'Schema Registry for Robot Framework',
      long_description = DESCRIPTION,
      author       = 'Pawel Kowalski',
      author_email = '<kowalski_pawel@hotmail.com>',
      url          = 'https://github.com/nestor-pl/robotframework-SchemaRegistryLibrary',
      license      = 'Apache License 2.0',
      keywords     = 'robotframework testing schema registry',
      platforms    = 'any',
      classifiers  = [
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Topic :: Software Development :: Testing"
      ],
      install_requires = [
          'robotframework >= 2.6.0',
          'kafka-python',
      ],
      packages    = ['SchemaRegistryLibrary'],
      )
