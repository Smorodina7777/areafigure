from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="areafigure",
    version="0.0.1",
    author="Elena Gorlanova",
    author_email="dima26031@yandex.ru",
    description="A package to get area of figure",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/areafigure/homepage/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.11.5",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)