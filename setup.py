from setuptools import setup
from setuptools import find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='CGvsPhoto',
      version='0.0.1',
      description='a simple example for set up a lib',
      long_description=readme(),
      url='https://github.com/JunFugithub/pytestexample',
      author='jfu',
      author_email='jfu@gmail.com',
      install_requires=['pandas>=0.23.0', 
                        'pytest>=3.6.2'],
      zip_safe=False)
