from distutils.core import Command
from distutils.errors import DistutilsOptionError
from os import path
from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.sdist import sdist
from shutil import which
import subprocess


class BuildWebpackBundle(Command):
    description = 'Install dependencies with Yarn and run Webpack'

    user_options = [
        ('webpack-environment=', None, 'Webpack environment ("development" or "production")')
    ]

    def initialize_options(self):
        self.webpack_environment = None

    def finalize_options(self):
        if self.webpack_environment not in ('development', 'production'):
            raise DistutilsOptionError('Must set the Webpack environment to either "development" or "production"; was {}'.format(
                    self.webpack_environment))

    def run(self):
        yarn = which('yarn') or which('yarn.cmd')
        if yarn is None:
            print('Failed to find yarn or yarn.cmd on PATH; aborting')
            return False

        subprocess.check_call([yarn, 'install'], cwd=root_dir)
        subprocess.check_call([yarn, 'run', 'webpack', '--mode', self.webpack_environment], cwd=root_dir)


class WithBuildWebpackBundle:
    user_options = [
        ('webpack-environment=', None, 'Webpack environment ("development" or "production")'),
    ]

    webpack_environment = None

    def initialize_options(self, default_webpack_environment):
        self.webpack_environment = default_webpack_environment

    def build_webpack_bundle(self, command_name):
        cmd = self.distribution.get_command_obj('build_webpack_bundle')
        cmd.set_undefined_options(command_name, ('webpack_environment', 'webpack_environment'))
        self.run_command('build_webpack_bundle')


class DevelopWithBuildWebpackBundle(develop, WithBuildWebpackBundle):
    user_options = develop.user_options + WithBuildWebpackBundle.user_options

    def initialize_options(self):
        super().initialize_options()
        WithBuildWebpackBundle.initialize_options(self, 'development')

    def install_for_development(self):
        super().install_for_development()
        WithBuildWebpackBundle.build_webpack_bundle(self, 'develop')


class SdistWithBuildWebpackBundle(sdist, WithBuildWebpackBundle):
    user_options = sdist.user_options + WithBuildWebpackBundle.user_options

    def initialize_options(self):
        super().initialize_options()
        WithBuildWebpackBundle.initialize_options(self, 'production')

    def make_distribution(self):
        WithBuildWebpackBundle.build_webpack_bundle(self, 'sdist')
        super().make_distribution()


root_dir = path.abspath(path.dirname(__file__))
with open(path.join(root_dir, 'README.md')) as f:
    long_description = f.read()

setup(
    name='mkdocs-theme-bootstrap4',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.3.0',
    cmdclass={
        'build_webpack_bundle': BuildWebpackBundle,
        'develop': DevelopWithBuildWebpackBundle,
        'sdist': SdistWithBuildWebpackBundle,
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
