from distutils.core import Command
from distutils.errors import DistutilsOptionError
from os import path
from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.sdist import sdist
import subprocess


class BuildWebpackBundle(Command):
    description = 'Install dependencies with Yarn and run Webpack'

    user_options = [
        ('webpack-environment=', None, 'Webpack environment ("development" or "production")')
    ]

    def initialize_options(self):
        self.webpack_environment = None

    def finalize_options(self):
        self.set_undefined_options('sdist', ('webpack_environment', 'webpack_environment'))
        if self.webpack_environment not in ('development', 'production'):
            raise DistutilsOptionError('Must set the Webpack environment to either "development" or "production"; was {}'.format(
                    self.webpack_environment))

    def run(self):
        subprocess.check_call(['yarn', 'install'], cwd=root_dir)
        subprocess.check_call(['yarn', 'run', 'webpack', '--mode', self.webpack_environment], cwd=root_dir)


def with_build_webpack_bundle(command_class, default_webpack_environment=None):
    class WithBuildWebpackBundle(command_class):
        def initialize_options(self):
            super().initialize_options()
            self.webpack_environment = default_webpack_environment

        def make_distribution(self):
            self.run_command('build_webpack_bundle')
            super().make_distribution()

    WithBuildWebpackBundle.user_options.append((
            'webpack-environment=', None, 'Webpack environment ("development" or "production")'))

    return WithBuildWebpackBundle


root_dir = path.abspath(path.dirname(__file__))
with open(path.join(root_dir, 'README.md')) as f:
    long_description = f.read()

setup(
    name='mkdocs-theme-bootstrap4',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.2.0',
    cmdclass={
        'build_webpack_bundle': BuildWebpackBundle,
        'develop': with_build_webpack_bundle(develop, 'development'),
        'sdist': with_build_webpack_bundle(sdist, 'production'),
    },
    packages=['mkdocs_bootstrap4'],
    package_data={
        'mkdocs_bootstrap4': [
            'dist/bundle.js',
            '404.html',
            'base.html',
            'content.html',
            'main.html',
            'mkdocs_theme.yml',
            'nav-sub.html',
            'search-modal.html',
            'toc.html',
        ],
    },
    url='https://github.com/LukeCarrier/mkdocs-theme-bootstrap4',
    license='MIT',
    author='Luke Carrier',
    author_email='luke@carrier.im',
    description='A vanilla Bootstrap 4 theme',
    install_requires=['mkdocs>=1.0'],
    entry_points={
        'mkdocs.themes': [
            'bootstrap4 = mkdocs_bootstrap4',
        ],
    },
    zip_safe=False,
)
