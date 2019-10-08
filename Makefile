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

.PHONY: clean coverage dist pdb pipclean piplist publish publish-test requirements shell test test-setup

clean:
	@rm -rf .eggs
	@rm -rf .tox
	@rm -rf build
	@rm -rf tempenv*.egg-info
	@rm -rf dist
	@find . -name '*.py,cover' | xargs rm -f
	@find . -name '*.pyc' | xargs rm -f
	@find . -name '__pycache__' | xargs rm -rf

coverage:
	tox -e coverage

dist: clean
	python3 setup.py sdist bdist_wheel

pdb:
	tox -- --pdb

pipclean:
	@rm -rf ~/.cache/pip
	@rm -rf ~/.local

piplist:
	pip3 list --user --format=columns

publish: dist
	twine check dist/*
	twine upload --username ${PYPI_USERNAME} --password ${PYPI_PASSWORD} dist/*

publish-test: dist
	twine check dist/*
	twine upload --username ${PYPI_USERNAME} --password ${PYPI_PASSWORD} --repository-url https://test.pypi.org/legacy/ dist/*

prerequisites:
	pip3 install -r requirements/dev.txt
	pre-commit install

shell:
	tox -e run -- bash

test: test-setup
	tox

test-setup:
	python3 setup.py check
