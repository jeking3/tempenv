# tempenv

[![pypi](https://img.shields.io/pypi/v/tempenv.svg)](https://pypi.python.org/pypi/tempenv)
[![Build Status](https://github.com/jeking3/tempenv/actions/workflows/ci.yml/badge.svg)](https://github.com/jeking3/tempenv/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/jeking3/tempenv/branch/main/graph/badge.svg)](https://codecov.io/gh/jeking3/tempenv)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

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

## Install

Install the latest version of tempenv:

```
pip install tempenv
```

## Examples

Each of these examples can be found in the tests.

Set some environment variables temporarily:
(see tests/example_set_test.py):

```python
def test_set(self):
    user_before = os.environ.get("USER")
    with TemporaryEnvironment({"USER": "nobody", "OTHER": "foo"}):
        assert os.environ.get("USER") == "nobody"
        assert os.environ.get("OTHER") == "foo"
    assert os.environ.get("USER") == user_before
```

Changing the value to ``None`` will unset the environment variable during
the code block
(see tests/example_unset_test.py):

```python
def test_unset(self):
    os.environ["DEBUG"] = "1"
    with TemporaryEnvironment({"DEBUG": None}):
        assert "DEBUG" not in os.environ
    assert "DEBUG" in os.environ
```

Changing a temporary environment variable during the scope will cause a
warning
(see tests/example_overwrite_test.py):

```python
def test_overwritten_in_context(self):
    with self.assertWarnsRegex(EnvironmentVariableChangedWarning, "FOO"):
        with TemporaryEnvironment({"FOO": "BAR"}):
            os.environ["FOO"] = "SAM"
```

If you set the optional argument ``restore_if_changed=False`` then a change
during the scope of the TemporaryEnvironment will not issue a warning and will
not restore to the original value
(see tests/example_ignore_test.py):

```python
def test_ignored_overwrite_in_context(self):
    os.environ["FOO"] = "BAR"
    with TemporaryEnvironment({"FOO": "SAM"}, restore_if_changed=False):
        os.environ["FOO"] = "DEAN"
    assert os.environ["FOO"] == "DEAN"
```

You can use TemporaryEnvironment in a unittest scope as follows
(see tests/example_unittest_test.py):

```python
@TemporaryEnvironment({"USER": "Crowley"})
def test_check(self):
    assert os.environ.get("USER") == "Crowley"
```

## License

Released under the Apache Software License, Version 2.0 (see `LICENSE`):

```
   Copyright (C) 2019 - 2022 James E. King III (@jeking3) <jking@apache.org>
```

## Bugs

Please report any bugs that you find on [GitHub](https://github.com/jeking3/tempenv/issues).
Or, even better, fork the repository on [GitHub](https://github.com/jeking3/tempenv)
and create a pull request (PR). We welcome all changes, big or small, and we
will help you make the PR if you are new to `git` (just ask on the issue and/or
see `CONTRIBUTING.rst`).
