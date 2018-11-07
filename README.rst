Photocurrent
============

Here we provide some guidelines to calculate photocurrent on semiconductor heterostructures.

It is intended to be a "how to" more than a "building block", so don't hesitate in copy useful parts and ignore the parts that don't make sense.

Preparing for Development
-------------------------

We used Python 3. It is possible that a few changes need to be done in order to use Python 2.

That said, we suggest using Python 3.6:

::

    $ sudo apt-get update
    $ sudo apt-get install build-essential libpq-dev libssl-dev openssl libffi-dev zlib1g-dev
    $ sudo apt-get install python3.6 python3-pip python3-dev
    $ sudo update-alternatives --install "/usr/bin/python" "python" "$(which python3.6)" 1500

Please take care with the last line, since it will make Python 3 your default Python. In case of that not working, you might try:

::

    $ sudo update-alternatives --set python /usr/bin/python3.6
    $ sudo pip3 install --upgrade pip

We recomment the use of a `virtualenv`_, which you can accomplish through:

::

    $ sudo pip install virtualenv

Now, please create an environment for Python 3:

::

    $ virtualenv --python=$(which python3.6) env
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

    (env) $ PYTHONPATH=./core && python -m unittest discover tests/

.. _virtualenv: https://virtualenv.pypa.io/en/latest/