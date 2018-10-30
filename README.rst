Photocurrent
============

Here we provide some guidelines to calculate photocurrent on semiconductor heterostructures.

It is intended to be a "how to" more than a "building block", so don't hesitate in copy useful parts and ignore the parts that don't make sense.

Preparing for Development
-------------------------

We used Python 3. It is possible that a few changes need to be done in order to use Python 2.

That said, we suggest using Python 3:

::

    $ sudo apt-get install python3 python3-pip
    $ update-alternatives --install "/usr/bin/python" "python" "$(which python3)" 1


Please take care with the last line, since it will make Python 3 your default Python.

We recomment the use of a `virtualenv`_, which you can accomplish through:

::

    $ sudo apt-get install virtualenv


Now, please create an environment for Python 3:

::

    $ virtualenv --python=$(which python3) env
    $ source env/bin/activate


After that, clone the repository and install it:

::

    (env) $ git clone https://github.com/thiagolcmelo/photocurrent
    (env) $ cd photocurrent
    (env) $ pip install .

Running Tests
-------------

Run tests locally with virtualenv active:

::

    $ PYTHONPATH=./core && python -m unittest discover tests/

.. _virtualenv: https://virtualenv.pypa.io/en/latest/