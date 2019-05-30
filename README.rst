tempenv
=======

.. image:: https://travis-ci.org/jeking3/tempenv.svg?branch=master
   :target: https://travis-ci.org/jeking3/tempenv

.. image:: https://ci.appveyor.com/api/projects/status/github/jeking3/tempenv?branch=master&svg=true
   :target: https://ci.appveyor.com/project/jeking3/tempenv

.. image:: https://codecov.io/gh/jeking3/tempenv/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/jeking3/tempenv

tempenv provides a
`context manager<https://docs.python.org/3/library/contextlib.html>_`
that allows environment variables to be set or unset temporarily
and returned to their original values at scope end.

You can:

- Set or unset environment variables inside a ``with`` code block,
- Get a warning if the code block modifies one of the environment
  variables,
- Optionally bypass restoration of the original environment variable
  value if the code block modifies the environment variable.

Install
-------

Install the latest version of tempenv::

    $ pip install tempenv

Example
-------

Set some environment variables temporarily:

.. code:: python

    import os
    from tempenv import TemporaryEnvironment

    print(f"USER (before) = {os.environ.get('USER')}")
    with TemporaryEnvironment({
        "SOMETHING": "abcdefg",
        "USER": "nobody"
    }):
        print(f"USER (inside) = {os.environ.get('USER')}")
    print(f"USER (after ) = {os.environ.get('USER')}")

.. code:: bash

    $ python3 test.py
    USER (before) = test
    USER (inside) = nobody
    USER (after ) = test

Changing the value to ``None`` will unset the environment
variable during the code block:

.. code:: python

    from tempenv import TemporaryEnvironment

    with TemporaryEnvironment({"DEBUG": None}):
        # do something
        pass

License
-------

Released under the Apache Software License, Version 2.0 (see `LICENSE`)::

   Copyright (C) 2019 James E. King III (@jeking3) <jking@apache.org>

Bugs
----

Please report any bugs that you find `here <https://github.com/jeking3/tempenv/issues>`_.
Or, even better, fork the repository on `GitHub <https://github.com/jeking3/tempenv>`_
and create a pull request (PR). We welcome all changes, big or small, and we
will help you make the PR if you are new to `git` (just ask on the issue and/or
see `CONTRIBUTING.rst`).
