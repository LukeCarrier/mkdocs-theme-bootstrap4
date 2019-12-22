# Bootstrap 4 theme for MkDocs

A vanilla Bootstrap 4 theme.

---

## Screenshot

<img style="max-width:100%;" alt="Screenshot of Bootstrap4 theme for MkDocs" src="screenshots/mkdocs-bootstrap4.png" align="center" /><br />

## Quick start

First install the package:

```
$ pip install mkdocs-theme-bootstrap4
```

Then enable it:

```yaml
theme:
    name: bootstrap4
```

## Configuration

Place these additional options under the `theme:` section of your `mkdocs.yml` configuration to change the theme's behaviour.

```yaml
# Show next/previous links between pages?
next_previous: true
```

## Hacking

First, install the dependencies:

* [Python 2](https://www.python.org/downloads/), for some of our dependencies.
* [Python 3](https://www.python.org/downloads/), for the package build process.
* [Yarn](https://yarnpkg.com/en/docs/cli/install), for managing frontend dependencies.

Ensure that Python 2 is found on your path before Python 3, else you'll get errors from `node-gyp` later. If you're unable to do this, set the environment variable `npm_config_python` to a command that'll launch Python 2 (`py -2` on Windows, `python2` elsewhere).

On Windows:

* It's easiest to not put Python on your path and instead rely on the [`py` CLI](https://docs.python.org/using/windows.html#python-launcher-for-windows).
* You'll need the build tools necessary to install native dependencies: `npm install -g --production windows-build-tools`.

To get completion working in your editor, set up a virtual environment in the root of this repository and install MkDocs:

```
$ pip3 install --user --upgrade setuptools twine wheel
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
```

To install the plugin onto a local MkDocs site in editable form:

```
$ pip install --editable /path/to/mkdocs-theme-bootstrap4
```

## Releasing

Build the distributable package:

```
$ python3 setup.py sdist bdist_wheel
```

Push it to the PyPI test instance:

```
$ python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

Test it inside a virtual environment:

```
$ pip install --index-url https://test.pypi.org/simple/ --no-deps mkdocs-drawio-exporter
```

Let's go live:

```
$ python3 -m twine upload dist/*
```
