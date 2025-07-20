from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    This Function will return list of requirements
    """
    requirement_list:List[str] = []
    try:
        with open('requirements.txt', 'r') as files:
            lines = files.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)        
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_list

print(get_requirements())

setup(
    name="AI_TRAVEL_PLANNER",
    version="0.0.1",
    author="Somesh Chitranshi",
    author_email="namanayo5@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements()
)