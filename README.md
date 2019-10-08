# tempenv

[![Build Status](https://travis-ci.org/jeking3/tempenv.svg?branch=master)](https://travis-ci.org/jeking3/tempenv)
[![codecov](https://codecov.io/gh/jeking3/tempenv/branch/master/graph/badge.svg)](https://codecov.io/gh/jeking3/tempenv)

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

Set some environment variables temporarily
(see [example_set_test.py](tests/example_set_test.py)):

```
    def test_set(self):
        user_before = os.environ.get("USER")
        with TemporaryEnvironment({"USER": "nobody", "OTHER": "foo"}):
            assert os.environ.get("USER") == "nobody"
            assert os.environ.get("OTHER") == "foo"
        assert os.environ.get("USER") == user_before
```

Changing the value to ``None`` will unset the environment variable during
the code block
(see [example_unset_test.py](tests/example_unset_test.py)):

```
    def test_unset(self):
        os.environ["DEBUG"] = "1"
        with TemporaryEnvironment({"DEBUG": None}):
            assert "DEBUG" not in os.environ
        assert "DEBUG" in os.environ
```

Changing a temporary environment variable during the scope will cause a
warning
(see [example_overwrite_test.py](tests/example_overwrite_test.py)):

```
    def test_overwritten_in_context(self):
        with self.assertWarnsRegex(EnvironmentVariableChangedWarning, "FOO"):
            with TemporaryEnvironment({"FOO": "BAR"}):
                os.environ["FOO"] = "SAM"
```

If you set the optional argument ``restore_if_changed=False`` then a change
during the scope of the TemporaryEnvironment will not issue a warning and will
not restore to the original value
(see [example_ignore_test.py](tests/example_ignore_test.py)):

```
    def test_ignored_overwrite_in_context(self):
        os.environ["FOO"] = "BAR"
        with TemporaryEnvironment({"FOO": "SAM"}, restore_if_changed=False):
            os.environ["FOO"] = "DEAN"
        assert os.environ["FOO"] == "DEAN"
```

You can use TemporaryEnvironment in a unittest scope as follows
(see [example_unittest_test.py](tests/example_unittest_test.py)):

```
    @TemporaryEnvironment({"USER": "Crowley"})
    def test_check(self):
        assert os.environ.get("USER") == "Crowley"
```

## License

Released under the Apache Software License, Version 2.0 (see `LICENSE`):

```
   Copyright (C) 2019 James E. King III (@jeking3) <jking@apache.org>
```

## History

### v0.2.0

- Added decorator support.
- Updated README with more examples.

### v0.1.0

- Initial release.

## Bugs

Please report any bugs that you find [here](https://github.com/jeking3/tempenv/issues).
Or, even better, fork the repository on [GitHub](https://github.com/jeking3/tempenv)
and create a pull request (PR). We welcome all changes, big or small, and we
will help you make the PR if you are new to `git` (just ask on the issue and/or
see `CONTRIBUTING.rst`).
