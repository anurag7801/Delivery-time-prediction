from setuptools import setup, find_packages
from typing import List


with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

REPO_NAME = 'Delivery-time-prediction'
PROJECT_NAME = "delivery_Prediction"
__version__ = "0.0.1"
DESCRIPTION = "This machine learning Project will predict the delivery timings"
AUTHOR_USER_NAME = "anurag7801"
AUTHOR_NAME = "Anurag Kumar"
AUTHOR_EMAIL = "anuragk7801@gamil.com"

REQUIREMENTS_FILE = 'requirements.txt'

def get_requirements_list()->List[str]:
    with open(REQUIREMENTS_FILE,"r") as require:
        strings = require.readlines()
        cleaned_strings = [
            string.strip() for string in strings  # Remove '\n' and leading/trailing whitespaces
            if string.strip() and not string.strip().startswith('#')  # Remove empty strings and those starting with '#'
            ]

    if "-e ." in cleaned_strings:
        cleaned_strings.remove("-e .")

    return cleaned_strings



setup(
    name=PROJECT_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    packages=find_packages(),
    install_requires = get_requirements_list()
    # package_dir={"": "src"},
    # packages=setuptools.find_packages(where="src")
)