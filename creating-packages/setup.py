from setuptools import setup, find_packages

VERSION="0.1.0.dev0"

setup(
    name="hello",
    version=VERSION,
    packages=find_packages("src"),
    package_dir={'': 'src'},
    include_package_data=True,
    )
