"""Setup.py."""
from setuptools import setup, find_packages
from cli import __version__
setup(
    name='databricks-workspace-cleaner',
    version=__version__,
    description='',
    url='',
    author='Luke Vinton',
    author_email='luvinton@microsoft.com',
    license='NA',
    packages=find_packages(),
    install_requires=['fire', 'databricks-cli', 'fire-cli-helper@git+https://github.com/frogrammer/fire-cli-helper.git'],
    tests_require=[],
    classifiers=[],
    test_suite='',
    entry_points={
        'console_scripts': [
            'dwc = cli.__main__:main',
        ],
    },
)
