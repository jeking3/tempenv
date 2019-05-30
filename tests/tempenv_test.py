# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 James E. King III (@jeking3) <jking@apache.org>
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

from unittest import TestCase

from tempenv import EnvironmentVariableChangedWarning
from tempenv import TemporaryEnvironment


class TestTemporaryEnvironment(TestCase):
    def setUp(self):
        for i in range(1, 4):
            os.environ[f"_TTE_{i}"] = str(i)
        self.check()

    @staticmethod
    def slot(num):
        return num - 1

    def check(self, expect=["1", "2", "3", None]):
        for i in range(1, len(expect) + 1):
            self.assertEqual(os.environ.get(f"_TTE_{i}"), expect[self.slot(i)])

    def test_create(self):
        """ Test temporarily setting an envvar. """
        with TemporaryEnvironment({"_TTE_4": "4"}):
            self.check(["1", "2", "3", "4"])
        self.check()

    def test_overwrite(self):
        """ Test overwriting an existing envvar. """
        with TemporaryEnvironment({"_TTE_2": "20"}):
            self.check(["1", "20", "3", None])
        self.check()

    def test_delete_existing(self):
        """ Test removing an existing envvar. """
        with TemporaryEnvironment({"_TTE_2": None}):
            self.check(["1", None, "3", None])
        self.check()

    def test_delete_not_existing(self):
        """ Test removing a non-existant envvar. """
        self.assertNotIn("_NONEXIST", os.environ)
        with TemporaryEnvironment({"_NONEXIST": None}):
            self.assertNotIn("_NONEXIST", os.environ)
            self.check()
        self.assertNotIn("_NONEXIST", os.environ)
        self.check()

    def test_overwritten_in_context(self):
        """ Test detection of overwritten value in context. """
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            with TemporaryEnvironment({"_TTE_2": "20"}):
                self.check(["1", "20", "3", None])
                os.environ["_TTE_2"] = "200"
            self.check()
            self.assertEqual(len(w), 1)
            self.assertIs(w[-1].category, EnvironmentVariableChangedWarning)
            self.assertIn("_TTE_2", str(w[-1].message))

    def test_overwritten_no_restore(self):
        """ Test handling of non-restore if overwritten. """
        with TemporaryEnvironment({"_TTE_2": "20"}, restore_if_changed=False):
            self.check(["1", "20", "3", None])
            os.environ["_TTE_2"] = "200"
        self.check(["1", "200", "3", None])
