from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in four_whats_net/__init__.py
from four_whats_net import __version__ as version

setup(
	name="four_whats_net",
	version=version,
	description="4Whats.net",
	author="hts-qatar",
	author_email="azim@htsqatar.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
