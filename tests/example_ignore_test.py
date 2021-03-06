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

from tempenv import TemporaryEnvironment


class TestIgnoreOverwrite(TestCase):
    # if you change this test, please update the README
    def test_ignored_overwrite_in_context(self):
        os.environ["FOO"] = "BAR"
        with TemporaryEnvironment({"FOO": "SAM"}, restore_if_changed=False):
            os.environ["FOO"] = "DEAN"
        assert os.environ["FOO"] == "DEAN"
