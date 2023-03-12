from pathlib import Path
from setuptools import find_namespace_packages, setup


BASE_DIR = Path(__file__).parent
with open(Path(BASE_DIR, "requirements.txt"), "r") as f:
    required_installs = [ln.strip() for ln in f.readlines()]


setup(
    name="testing",
    version=1.0.0,
    author= ['testing'],
    install_requires=[required_installs],
    packages=find_namespace_packages(),
    description="testing",
    keywords="testing",
    url="testing"
)