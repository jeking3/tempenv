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
# begin
import os

from unittest import TestCase

from tempenv import EnvironmentVariableChangedWarning
from tempenv import TemporaryEnvironment


class TestOverwrite(TestCase):
    # if you change this test, please update the README
    def test_overwritten_in_context(self):
        with self.assertWarnsRegex(EnvironmentVariableChangedWarning, "FOO"):
            with TemporaryEnvironment({"FOO": "BAR"}):
                os.environ["FOO"] = "SAM"
