from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = "-e ."
#define a function to get the requirements
def get_requirements(file_path:str)->List[str]:
    """
    this is a function that gets the requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

setup(
    name = "ml_project",
    version = "0.0.1",
    author = "E Azi-love",
    email = "aziloveemma@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt")
)