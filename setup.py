from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in pms/__init__.py
from pms import __version__ as version

setup(
	name="pms",
	version=version,
	description="patient managment system",
	author="krupal vora",
	author_email="krupal vora",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
