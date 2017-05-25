# Doctests Are Magical

Kill two birds with one stone by writing doctests that can be used as unittests and documentation!

This repository is an example I wrote for a [PyMNtos](https://www.meetup.com/PyMNtos-Twin-Cities-Python-User-Group/) talk of mine.

This repo uses Python 3.

## What you'll learn

  * Using doctests as unit tests
  * Extending and configuring `py.test`
  * Using Sphinx to create documentation, utilizing docstrings from code

## Tutorial

Here's a step-by-step guide you can follow!

Also very useful for my own notes while talking.

I'm using Ubuntu in this tutorial.

### Step one: setup!

```shell
git clone git@github.com:lily-mayfield/example-doctests-sphinx-testing.git
cd example-doctests-sphinx-testsing

# Now create a virtual environment for this repo. Here I include how to
# install virtualenvwrapper, which is my preferred way of managing
# virtual environments.
sudo apt install python-pip
pip install virtualenvwrapper
echo 'export WORKON_HOME=$HOME/.virtualenvs' >> ~/.bashrc
echo 'export PROJECT_HOME=$HOME/Devel' >> ~/.bashrc
echo 'source /home/lily/.local/bin/virtualenvwrapper.sh' >> ~/.bashrc
. ~/.bashrc
mkvirtualenv doctest-demo -p python3

```

### Configure Sphinx

```shell
# Now that we're in our virtual environment let's install the rest of
# the tools we'll need...
pip install sphinx pytest sphinxcontrib-napoleon

# Now let's create our sphinx docs!
# It will ask root path for documentation, say "docs". Also, I prefer
# to "separate source and build directories". The defaults are great
# for everything else, but don't forget a project name, author name.
# Oh and "> autodoc: automatically insert docstrings from modules (y/n) [n]:"
# say "yes."
# > doctest: automatically test code snippets in doctest blocks (y/n) [n]: y
# > intersphinx: link between Sphinx documentation of different projects (y/n)
# [n]: y
# > coverage: checks for documentation coverage (y/n) [n]: y
# you may wanna note > githubpages: create .nojekyll file to publish the
# document on GitHub pages (y/n) [n]:, but most people use readthedocs
sphinx-quickstart
```

Edit `docs/source/conf.py` and find the python list `extensions`, add
`'sphinxcontrib.napoleon',` to it. This is because we're going to use Google Style
Docstrings, instead of the default ugly/illegible docstring code formatting.

Edit `docs/source/conf.py` again to add the package directory we're testing to
sphinx (you can comment-out these lines in config, but you have to edit the path:

```python
# These three lines below I uncommented.
# Also, I modified the last line to insert ../.. to PATH.
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
```

Make a file called `docs/source/index.rst`:

```rst
Welcome to Magical Doctest Demo Docs!
=====================================

Here is the homepage of your documentation!

Contents:

.. toctree::
   :maxdepth: 2

   doctestdemo

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

```

Make another file `docs/source/doctestdemo.rst`:

```rst
Doctest Demos
=============

.. py:module:: doctestdemo.animals

.. automodule:: doctestdemo.animals

Animal overview
-----------------------

An :class:`Animal` is a base class that all animals, such as :class:`Cat` and
:class:`Dog` inherit from.

Here's what an `Animal` looks like:

.. autoclass:: Animal

```

Excellent! You should be able to make your docs with `make html` and view them
by opening `docs/build`.

### Unit Tests, py.test doctests

Run all the tests like this:

`py.test tests --doctest-modules doctestdemo`

You can actually make a `py.test` configuration file:

```
# content of pytest.ini
[pytest]
addopts = --doctest-modules
doctest_optionflags = ELLIPSIS
```

### In closing

Now you have docs in two places: in the code itself and in your nice web docs,
plus you now have more unit tests! Whoah!

Some goodies to improve any project:

  * [`typing`: support for type hints](https://docs.python.org/3/library/typing.html)
  * Code Climate
  * Travis CI
  * `pytest-pep8`
  * Code coverage! I love `pytest-cov` + `python-coveralls`,
    [coveralls.io](coveralls.io).
  * [Be sure to read the Sphinx `autodoc` page!](http://www.sphinx-doc.org/en/stable/ext/autodoc.html)
  * [Be sure to also read the pytest doctest integrations page](https://docs.pytest.org/en/latest/doctest.html)

