from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns the list of requirements.
    '''
    requirements = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file_obj:
            requirements = file_obj.readlines()
            requirements = [req.strip() for req in requirements if req.strip()]

            if HYPHEN_E_DOT in requirements:
                requirements.remove(HYPHEN_E_DOT)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    except Exception as e:
        print(f"An error occurred while reading {file_path}: {e}")
    
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Roshan',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)