# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [2.1.0]

- dropped python 3.7 and 3.8 (ci tests 3.9 through 3.13)
- updated dev and test dependencies (still no runtime dependencies)
- updated setup.py constructs

## [2.0.0]

- convert to using ContextDecorator @jeking3 in #22
- fixed incorrect type on initializer (value was not optional)
- dropped python 3.6 support (ci tests 3.7 through 3.10)
- update dev and test dependencies (still no runtime dependencies)

## [1.1.0]

### Changed

- Added PEP 561 compliant typing (and trove identifier)
- Added mypy in pre-commit and fixed one errant type.

## [1.0.0]

### Changed

- Move CI from Travis to GitHub
- Enable Dependabot

## [0.2.0]

### Added

- Added decorator support.

### Changed

- Updated README with more examples.

## [0.1.0]

### Added

- Initial release.
