from setuptools import find_packages
from setuptools import setup

setup(
    name='mycobot_gazebo',
    version='0.0.0',
    packages=find_packages(
        include=('mycobot_gazebo', 'mycobot_gazebo.*')),
)
