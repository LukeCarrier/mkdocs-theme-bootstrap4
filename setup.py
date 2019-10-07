from setuptools import setup
from os import path


root_dir = path.abspath(path.dirname(__file__))
with open(path.join(root_dir, 'README.md')) as f:
    long_description = f.read()

setup(
    name='mkdocs-bootstrap4',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.1.2',
    packages=['mkdocs_bootstrap4'],
    url='https://github.com/byrnereese/mkdocs-bootstrap4/',
    license='MIT',
    author='Byrne Reese',
    author_email='byrne@majordojo.com',
    description='A vanilla Bootstrap 4 theme',
    install_requires=['mkdocs>=1.0'],
    entry_points={
        'mkdocs.themes': [
            'bootstrap4 = mkdocs_bootstrap4',
        ],
    },
    zip_safe=False,
)
