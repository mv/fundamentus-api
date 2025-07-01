# vim:ft=make:ts=8:sts=8:sw=8:noet:tw=80:nowrap:list

###
### Reference Makefile for Python stuff
###
### Mv: ferreira.mv[ at ]gmail.com
### 2019-07
###


# My vars: simple
_this := $(shell uname -sr)
_venv := venv
#python_version := 3.7.1
_python_version := $(shell python -V)

# My vars: recursive

_dt = $(warning 'Invoking shell')$(shell date +%Y-%m-%d.%H:%M:%S)


###
### targets/tasks
###
.DEFAULT_GOAL:= help
.PHONY: help show clean venv venv-clean

help:   ## - Default goal: list of targets in Makefile
help:   show
	@grep -E '^[a-zA-Z][a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
	    | awk 'BEGIN {FS = ":.*?## "}; {printf "  make \033[01;33m%-18s\033[0m %s\n", $$1, $$2}' \
	    | sort
	@echo


show:   ## - Show my vars
	@echo
	@echo "  This: [$(_this)]"
	@echo "  Virtualenv: [$(_venv)]"
	@echo "  Python Version: [$(_python_version)]"
	@echo


venv:   ## - Create virtualenv
	pip3 install virtualenv	   && \
	virtualenv $(_venv)        && \
	source venv/bin/activate   && \
	pip3 install --upgrade pip wheel setuptools pipenv

venv-clean: ## - Clean: rm virtualenv
	/bin/rm -rf $(_venv)


.PHONY: pip
pip:    ## - Install/upgrade Pip stuff
	pip3 install --upgrade pip wheel setuptools pipenv

.PHONY: pip-src
pip-src: ## - Pip install src/ (dev/editable)
	pip3 install -e .
	@echo
	pip3 list | egrep -i '^Package|^---|^fundamentus'
	@echo

.PHONY: req
req:    ## - Pip install from requirements.txt
	. $(_venv)/bin/activate              && \
	pip3 install -r requirements.txt


.PHONY: req-dev
req-dev: ## - Pip install from requirements-dev.txt
	. $(_venv)/bin/activate              && \
	pip3 install -r requirements-dev.txt


.PHONY: clean
clean:	## - Cleanup: pycache stuff
	find . -type d -name __py*cache__ -exec rm -rf {} \; 2>/dev/null
	find . -type f | egrep -i '.pyc|.pyb' | xargs rm
	rm -rf .pytest_cache
	rm -rf .ipynb_checkpoints
	rm -rf dist/*


.PHONY: test
test:   ## - Test: pytest
	pytest tests/ -q --color=yes


.PHONY: testd
testd: ## - Test: pytest many details
	coverage run --source=fundamentus -m \
	  pytest tests/ -v --color=yes && \
	coverage report -m

.PHONY: test-bash
test-bash:   ## - Test: bash calling sample scripts
	LOGLEVEL=info /usr/bin/time ./tests/test-scripts.sh


.PHONY: data
data:	## - Save generated files to data/
	/bin/mv -f *.csv *xls? *ods ?.txt ??.txt ???.txt data/ || true


.PHONY: data-clean
data-clean: ## - Clean data/
	/bin/rm -f data/*.*


.PHONY: pkg
pkg:	## - Package dist: create in dist/
	python setup.py sdist bdist_wheel

.PHONY: pkg-upload-testpypi
pkg-upload-testpypi: ## - PyPI: upload to Test
	twine upload --repository testpypi --verbose dist/*

.PHONY: pkg-upload-pypi
pkg-upload-pypi: ## - PyPI: upload to Test
	twine upload --repository pypi     --verbose dist/*

