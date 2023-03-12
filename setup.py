# setup.py
from pathlib import Path
from setuptools import find_namespace_packages, setup


BASE_DIR = Path(__file__).parent
with open(Path(BASE_DIR, "requirements.txt"), "r") as file:
    required_packages = [ln.strip() for ln in file.readlines()]


setup(
    name="torchtemplates",
    version=0.1, 
    description="A package to create pytorch projects quickly",
    author="Aneesh Aparajit G",
    author_email="aneeshaparajit.g2002@gmail.com",
    install_requires=[required_packages],
    packages=find_namespace_packages(), 
    entry_points={
        'console_scripts': [
            'torchtemplates=torchtemplates.torchtemplates:torchtemplates',
        ]
    }
)
