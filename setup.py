from setuptools import setup, find_packages

setup(
	name = 'od-logger',
	version = '1.0.0',
  packages = find_packages(),
  install_requires = [
    'certifi==2022.9.24',
    'charset-normalizer==2.1.1',
    'idna==3.4',
    'requests==2.28.1',
    'urllib3==1.26.12',
  ],
)