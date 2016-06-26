from setuptools import setup
from setuptools import find_packages

setup(
    name='RPi IO',
    version='0.01',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)
