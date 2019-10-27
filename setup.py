import os

from io import open
from setuptools import setup, find_packages


here = os.path.dirname(__file__)

with open(os.path.join(here, 'README.rst'), 'r', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='metispi',
    description='In brightest day in blackest night no evil shall escape your sight!',
    long_description=long_description,
    license='MIT',
    url='https://github.com/lotrien/metis',
    keywords='RaspberryPi RPi motion sensor',
    author='Olha Kurkaiedova',
    author_email='olya.kurkaedova@gmail.com',
    packages=find_packages(exclude=['docs', 'tests*']),
    use_scm_version=True,
    setup_requires=[
        'setuptools_scm',
    ],
    install_requires=[
        'RPi.GPIO >= 0.6.3',
        'gpiozero >= 1.3.2',
        'picamera >= 1.13',
        'blinker >= 1.4',
        'python-telegram-bot >= 6.1.0',
        'pyyaml >= 3.12',
    ],
)
