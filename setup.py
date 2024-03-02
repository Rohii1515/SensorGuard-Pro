from setuptools import find_packages, setup
from typing import List


# def get_requirements() -> list[str]:
#     """
#     This function returns a list of requirements
#     """
#     requirements_list: list[str] = []
#     with open('requirements.txt', 'r') as file:
#         for line in file:
#             # Remove leading and trailing whitespace
#             requirement = line.strip()
#             if requirement:
#                 requirements_list.append(requirement)

#     return requirements_list


setup(
    name="sensor",
    version="0.0.1",
    author="Rohii1515",
    author_email="rohidasjondhale1515@gmail.com",
    packages=find_packages(),
    install_requires= ["pymongo"]#get_requirements(),
)
