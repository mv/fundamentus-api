# vim:ft=make:ts=8:sts=8:sw=8:noet:tw=80:nowrap:list

###
### Reference Makefile for Python stuff
###
### Mv: ferreira.mv[ at ]gmail.com
### 2016-06
###

# My vars: simple
_os             := $(shell uname -sr)
_venv           := .venv
_python_version := $(shell python -V)

_pkg_name    := fundamentus
_pkg_repo    := mv/fundamentus-api
_pkg_version := $(shell awk -F" = " '/version/ {print $$2}' src/$(_pkg_name)/__init__.py | tr -d "'")

.DEFAULT_GOAL:=help

################################################################################
##@ Help
.PHONY: help
help:   ## - Default goal: list of targets in Makefile
	@make show
	@awk '\
	  BEGIN { FS = ":.*##"; printf "\nUsage:\n  make \033[01;33m<target>\033[0m\n" }        \
	  /^##@/                  { printf "\n\033[01;37m  %s   \033[0m\n"   , substr($$0, 5) } \
	  /^[a-zA-Z0-9_-]+:.*?##/ { printf "  \033[01;33m  %-25s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)
	@echo

.PHONY: show
show:   ## - Show header vars
	@echo
	@echo "  ## OS             [${_os}]"
	@echo "  ## Python Version [${_python_version}]"
	@echo "  ## Virtualenv     [${_venv}]"
	@echo "  ## Pkg Name       [${_pkg_name}]"
	@echo "  ## Pkg Repo       [${_pkg_repo}]"
	@echo "  ## Pkg Version    [${_pkg_version}]"
	@echo


################################################################################
##@ Virtualenv

venv:   ## - virtualenv: create
	python3 -m venv $(_venv) && \
	source $(_venv)/bin/activate   && \
	pip3 install --upgrade pip

venv-clean: ## - virtualenv: clean
	/bin/rm -rf $(_venv)

.PHONY: pip
pip:    ## - Pip install from requirements.txt
	. $(_venv)/bin/activate && \
	pip3 install -r requirements.txt

.PHONY: pip-dev
pip-dev: ## - Pip install from requirements-dev.txt
	. $(_venv)/bin/activate && \
	pip3 install -r requirements-dev.txt

.PHONY: pip-edit
pip-edit: ## - Pip install editable
	. $(_venv)/bin/activate && \
	python -m pip install --editable .

	@make _pip-show

.PHONY: pip-from-sdist
pip-from-sdist: ## - Pip install tar.gz
	export _ver=$$( cat src/$(_pkg_name)/__init__.py  | awk -F' = ' '/__version__/ {print $$2}' | tr -d "'" ) && \
	pip3 uninstall -y $(_pkg_name) && \
	pip3 install ./dist/$(_pkg_name)-$${_ver}.tar.gz

	@make _pip-show

.PHONY: pip-from-testpypi
pip-from-testpypi: ## - Pip install latest from TestPyPI
	pip3 uninstall -y $(_pkg_name) && \
	pip install --index-url https://test.pypi.org/simple/ $(_pkg_name)

	@make _pip-show

.PHONY: pip-from-pypi
pip-from-pypi: ## - Pip install latest from PyPI
	pip3 uninstall -y $(_pkg_name) && \
	pip install $(_pkg_name)

	@make _pip-show

## __internal__
.PHONY: _pip-show
_pip-show:
	@echo
	@pip3 list | egrep -i -A1 -B1 '^Package|^---|^fundamentus'
	@echo


################################################################################
##@ PyPi Package

# https://packaging.python.org/en/latest/overview/#python-source-distributions
#   sdist: source distribution: Pure Python code
#   wheel: binary distribution: Python + [Compiled C | Other languages]
.PHONY: build
build: ## - Pkg: build package
	@echo
	python3 -m build
#	hatch build
#	uv build

.PHONY: builds
builds: ## - Pkg: build --sdist
	@echo
	python3 -m build --sdist

.PHONY: buildw
buildw: ## - Pkg: build --wheel
	@echo
	python3 -m build --wheel

.PHONY: publish
publish: ## - TestPyPI: publish
#	twine upload --repository testpypi --verbose dist/*
	export UV_PUBLISH_PASSWORD=$$(cat ~/.pypirc | awk '/\[testpypi\]/,/^$$/' | awk -F= '/password/ {print $$2}') && \
	uv publish --index testpypi --username __token__

.PHONY: publish-pypi
publish-pypi: ## - PyPI: publish
#	twine upload --repository pypi     --verbose dist/*
	export UV_PUBLISH_PASSWORD=$$(cat ~/.pypirc | awk '/\[pypi\]/,/^$$/' | awk -F= '/password/ {print $$2}') && \
	echo uv publish --username __token__



################################################################################
##@ Version

.PHONY: version
version: ## - tbump: --only-patch: from 'tbump.toml' > to all files
	_version=$$(awk -F= '/version =/ {print $$2}' pyproject.toml | tr -d '" ') && \
	tbump --non-interactive --only-patch $${_version}

.PHONY: version-dry-run
version-dry-run: ## - tbump: --dry-run
	_version=$$(awk -F= '/version =/ {print $$2}' pyproject.toml | tr -d '" ') && \
	tbump --dry-run $${_version} || true

.PHONY: version-push
version-tag: ## - tbump: version > tag > commit > push
	_version=$$(awk -F= '/version =/ {print $$2}' pyproject.toml | tr -d '" ') && \
	tbump --non-interactive $${_version}


################################################################################
##@ Test

.PHONY: test
test:   ## - Test: Silent
	pytest tests/ -q --color=yes


.PHONY: testd
testd: ## - Test: Detailed
	coverage run --source=fundamentus -m \
	  pytest tests/ -v --color=yes && \
	coverage report -m

.PHONY: test-bash
test-bash:   ## - Test: bash calling sample scripts
	LOGLEVEL=info /usr/bin/time ./tests/test-scripts.sh


################################################################################
##@ Others

.PHONY: clean
clean:	## - Cleanup: pycache stuff
	find . -type d -name __py*cache__ -exec rm -rf {} \; 2>/dev/null || true
	find . -type f | egrep -i '.pyc|.pyb' | xargs rm || true
	rm -rf .pytest_cache      || true
	rm -rf .ipynb_checkpoints || true
	rm -rf dist/*             || true

.PHONY: data
data:	## - Save generated files to data/
	/bin/mv -f *.csv *xls? *ods ?.txt ??.txt ???.txt data/ || true


.PHONY: data-clean
data-clean: ## - Clean data/
	/bin/rm -f data/*.*

