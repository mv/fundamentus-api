# vim:ft=make:ts=8:sts=8:sw=8:noet:tw=80:nowrap:list

###
### Reference Makefile for Python stuff
###
### Mv: ferreira.mv[ at ]gmail.com
### 2019-07
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

venv:   ## - Create virtualenv
	virtualenv $(_venv)        && \
	source $(_venv)/bin/activate   && \
	pip3 install --upgrade pip wheel setuptools pipenv

venv-clean: ## - Clean: rm virtualenv
	/bin/rm -rf $(_venv)


.PHONY: pip
pip:    ## - Pip install from requirements.txt
	. $(_venv)/bin/activate              && \
	pip3 install --upgrade pip wheel setuptools pipenv && \
	pip3 install -r requirements.txt

.PHONY: pip-dev
pip-dev: ## - Pip install from requirements-dev.txt
	. $(_venv)/bin/activate              && \
	pip3 install -r requirements-dev.txt

.PHONY: pip-src
pip-src: ## - Pip install src/ (dev/editable)
	. $(_venv)/bin/activate              && \
	pip3 install -e .

	@echo
	@pip3 list | egrep -i -A1 -B1 '^Package|^---|^fundamentus'
	@echo



################################################################################
##@ Data: csv files et al.

.PHONY: data
data:	## - Save generated files to data/
	/bin/mv -f *.csv *xls? *ods ?.txt ??.txt ???.txt data/ || true


.PHONY: data-clean
data-clean: ## - Clean data/
	/bin/rm -f data/*.*

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
##@ PyPi Package

.PHONY: pkg
pkg:	## - Package dist: create in dist/
	python setup.py sdist bdist_wheel

.PHONY: pkg-upload-pypi
pkg-upload-pypi: ## - PyPI: upload
	twine upload --repository pypi     --verbose dist/*

.PHONY: pkg-upload-testpypi
pkg-upload-testpypi: ## - PyPI: upload to Test
	twine upload --repository testpypi --verbose dist/*



################################################################################
##@ Others

.PHONY: clean
clean:	## - Cleanup: pycache stuff
	find . -type d -name __py*cache__ -exec rm -rf {} \; 2>/dev/null
	find . -type f | egrep -i '.pyc|.pyb' | xargs rm
	rm -rf .pytest_cache
	rm -rf .ipynb_checkpoints
	rm -rf dist/*
