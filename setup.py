#!./.env/bin/python
from setuptools import setup, find_packages

CLASSIFIERS = [
  'Environment :: Web Environment'
]

setup(
  name='tci',
  author='Chase Ries',
  author_email='hello@chaseries.com',
  description='Just checking things out',
  license='BSD',
  version='0.1.0',
  url='https://github.com/chaseries/tci',
  packages=find_packages(),
  classifiers=CLASSIFIERS,
  platforms=['any'],
  install_requires=[],
  test_suite='tci.tests.suite',
  include_package_data=True,
  use_2to3=False,
  zip_safe=True
    )
