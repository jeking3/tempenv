# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 - 2022 James E. King III (@jeking3) <jking@apache.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import warnings

from contextlib import ContextDecorator
from typing import Dict
from typing import Optional


class EnvironmentVariableChangedWarning(ResourceWarning):
    """
    An environment variable being managed by a TemporaryEnvironment was
    changed by the context it was managing.
    """

    pass


class TemporaryEnvironment(ContextDecorator):
    """
    Manages a temporary environment.

    Sets or removes environment variables when entering, and will undo those
    changes on exit.  It does not save the entire environment, it will only
    modify the items it was directed to modify.

    If an environment variable is part of the directives and is changed
    by the context being managed, a warning is issued.
    """

    def __init__(
        self, directives: Dict[str, Optional[str]], restore_if_changed: bool = True
    ) -> None:
        """
        Initializer.

        Arguments:
            directives (Dict[str, str]):
                A list of environment variables to add/overwrite or
                remove.  To remove an environment variable set the value
                to None.  To remove the content of an environment variable
                but leave it defined, set the value to str().
            restore_if_changed (bool):
                Restore each tracked environment variable to the original state
                even if it was changed during the context.
        """
        # arguments
        self.directives = directives
        self.restore_if_changed = restore_if_changed

        # internals
        self._originals: Dict[
            str, Optional[str]
        ] = {}  # key: envvar name, value: string or None (not there)

    def __enter__(self) -> None:
        """
        Entering scope.

        Add any additions and remove any removals from the environment.
        Save the original values for restoration later.
        """
        for ename, dvalue in self.directives.items():
            self._originals[ename] = os.environ.get(ename)
            if dvalue is not None:
                os.environ[ename] = dvalue
            elif ename in os.environ:
                del os.environ[ename]

    def __exit__(self, *exc) -> None:
        """
        Leaving scope.

        Check for any changes and issue warnings if required, then restore
        things to their proper state if required.
        """
        for ename, ovalue in self._originals.items():
            dvalue = self.directives[ename]
            evalue = os.environ.get(ename)
            if evalue != dvalue:
                warnings.warn(ename, EnvironmentVariableChangedWarning)
                if not self.restore_if_changed:
                    continue
            if evalue != ovalue:
                if ovalue is not None:
                    os.environ[ename] = ovalue
                else:
                    del os.environ[ename]
