import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md'), 'r') as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='drf-nested-multipart-parser',
    version='0.0.1',
    license='MIT',
    packages=['drf_nested_multipart_parser'],
    include_package_data=True,
    description='Parser for nested params in multipart file upload',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/mick912/drf_nested_mutipart_parser.git',
    author='Mirjan Asymbaev',
    author_email='mirjan.asymbaev@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'License :: OSI Approved :: MIT License'
    ],
    python_requires='>=3.6',
)
