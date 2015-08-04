from setuptools import setup, find_packages

setup(
    name="double_down",
    version="0.1.1",
    author="Stephen Melnicki",
    author_email="smelnicki3@gmail.com",
    packages=find_packages(),
    description="A silly example of a python decorator",
    long_description=open("README.rst").read(),
    license="MIT (See LICENSE.rst)",
    url="https://github.com/smelnicki/double_down",
)
