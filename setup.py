from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    with open (file_path) as f:
        requirements=f.readlines()
        requirements=[r.replace('\n',"") for r in requirements]
        
        
setup(
   name='ReCall',
   version='0.0.1',
   description='Ann Churn Prediction model',
   author='Abir Chakraborty',
   author_email='abirc504@gmail.com',
   packages=find_packages(),  #same as name
   install_requires=get_requirements('requirements.txt')
)

