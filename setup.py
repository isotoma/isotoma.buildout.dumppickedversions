# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = "0.4"

long_description = (
    read('README.txt')
    + '\n' + 
    'Detailed Documentation\n'
    '======================\n'
    + '\n' +
    read('src', 'isotoma', 'buildout', 'dumppickedversions', 'pickedversions.txt')
    + '\n' +
    read('CHANGES.txt')
    + '\n' +
    read('CONTRIBUTORS.txt')
    )
entry_point = 'isotoma.buildout.dumppickedversions:install'
entry_points = {"zc.buildout.extension": ["default = %s" % entry_point]}

tests_require=['zc.buildout', 'zope.testing', 'zc.recipe.egg']

setup(name='isotoma.buildout.dumppickedversions',
      version=version,
      description="Dump buildout picked versions.",
      long_description=long_description,
      classifiers=[
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
      license='GPL',
      keywords='buildout extension dump picked versions',
      author='Chris Hannam',
      author_email='chris.hannam@isotoma.com',
      url='http://pypi.python.org/pypi/isotoma.buildout.dumppickedversions',
      packages = find_packages('src'),
      package_dir = {'':'src'},
      namespace_packages=['isotoma', 'isotoma.buildout'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'zc.buildout'
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite = 'isotoma.buildout.dumppickedversions.tests.test_suite',
      entry_points=entry_points,
      )
