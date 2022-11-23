from setuptools import setup, find_packages

setup(
	name = 'od-logger',
	version = '1.0.0',
  packages = find_packages(),
  install_requires = [
    'pika==1.3.1',
  ],
)