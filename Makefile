#
# Copyright (C) 2019 James E. King III (@jeking3) <jking@apache.org>
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

dist: clean coverage
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
	twine upload dist/*

publish-test: dist
	twine check dist/*
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

requirements:
	pip3 install -r requirements/dev
	pre-commit install

shell:
	tox -e run -- bash

test: test-setup
	tox

test-setup:
	python3 setup.py check
