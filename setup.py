# setup.py
from pathlib import Path
from setuptools import find_namespace_packages, setup


BASE_DIR = Path(__file__).parent
with open(Path(BASE_DIR, "requirements.txt"), "r") as file:
    required_packages = [ln.strip() for ln in file.readlines()]

this_directory = Path(__file__).parent
long_description = (this_directory / "pypi_readme.md").read_text()

setup(
    name="torchtemplates",
    version='1.0.1', 
    description="A package to create pytorch projects quickly",
    author="Aneesh Aparajit G",
    author_email="aneeshaparajit.g2002@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[required_packages],
    packages=find_namespace_packages(), 
    entry_points={
        'console_scripts': [
            'torchtemplates=torchtemplates.torchtemplates:torchtemplates',
        ]
    }, 
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3'
    ],
)
