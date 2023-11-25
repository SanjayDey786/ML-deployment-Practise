    ## setup.py = We will be able to build entire ML package and acan be used simply by intalling it as a package ##

from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='ML_deployment_practise',
version='0.0.1',
author='sanjay',
author_email='deysanjay30@gmail.com',
packages=find_packages(), ##here it will check mainly the src folder and other folders if it has __init__ constructors to build the package, so we have to create atleast the src folder and then the constructor within it
install_requires=get_requirements('requirements.txt')

)