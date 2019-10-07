# Bootstrap 4 theme for MkDocs

A vanilla Bootstrap 4 theme.

---

## Screenshot

<img style="max-width:100%;" alt="Screenshot of Bootstrap4 theme for MkDocs" src="screenshots/mkdocs-bootstrap4.png" align="center" /><br />

## Quick start

First install the package:

```
$ pip install mkdocs-bootstrap4
```

Then enable it:

```yaml
theme:
    name: bootstrap4
```

## Configuration

```yaml
# Show next/previous links between pages?
next_previous: true

# Keyboard shortcuts
shortcuts:
  help: 191    # ?
  next: 78     # n
  previous: 80 # p
  search: 83   # s
```

## Hacking

To get completion working in your editor, set up a virtual environment in the root of this repository and install MkDocs:

```
$ pip3 install --user --upgrade setuptools twine wheel
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
```

To install the plugin onto a local MkDocs site in editable form:

```
$ pip install --editable /path/to/mkdocs-bootstrap4
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
