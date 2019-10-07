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


class TestUnset(TestCase):
    # if you change this test, please update the README
    def test_unset(self):
        os.environ["DEBUG"] = "1"
        with TemporaryEnvironment({"DEBUG": None}):
            assert "DEBUG" not in os.environ
        assert "DEBUG" in os.environ
