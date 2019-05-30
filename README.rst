tempenv
=======

.. image:: https://travis-ci.org/jeking3/tempenv.svg?branch=master
   :target: https://travis-ci.org/jeking3/tempenv

.. image:: https://codecov.io/gh/jeking3/tempenv/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/jeking3/tempenv

Manage environment variables in a temporary scope.

Some products use environment variables as a primary means to supply
credentials.  To ensure the lifetime of exposed credentials is short,
wrap them in a TemporaryEnvironment so that they are automatically
destroyed on scope exit.

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

Then run the code:

.. code:: bash

    $ python3 test.py
    USER (before) = None
    USER (inside) = nobody
    USER (after ) = None

Changing the value to ``None`` will unset the environment
variable during the code block:

.. code:: python

    import os
    from tempenv import TemporaryEnvironment

    os.environ["DEBUG"] = "1"
    with TemporaryEnvironment({"DEBUG": None}):
        assert "DEBUG" not in os.environ
    assert "DEBUG" in os.environ

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
