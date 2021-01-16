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
.PHONY: help show clean pip pip-dev venv venv-clean data data-clean #pyenv

help:   ## - Default goal: list of targets in Makefile
help:   show
	@grep -E '^[a-zA-Z][a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
	    | awk 'BEGIN {FS = ":.*?## "}; {printf "  make \033[01;33m%-10s\033[0m %s\n", $$1, $$2}' \
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

pip:    ## - Install/upgrade Pip stuff
	pip3 install --upgrade pip wheel setuptools pipenv

pip-src: ## - Pip install src/ (dev/editable)
	pip3 install -e .
	@echo
	pip3 list | egrep -i '^Package|^---|^fundamentus'
	@echo

req:    ## - Pip install from requirements.txt
	. $(_venv)/bin/activate              && \
	pip3 install -r requirements.txt


req-dev: ## - Pip install from requirements_dev.txt
	. $(_venv)/bin/activate              && \
	pip3 install -r requirements_dev.txt


clean:	## - Cleanup: pycache stuff
	find . -type d -name __py*cache__ -exec rm -rf {} \; 2>/dev/null
	find . -type f | egrep -i '.pyc|.pyb' | xargs rm
	rm -rf .pytest_cache
	rm -rf .ipynb_checkpoints
	rm -rf dist/*


test:   ##    - Test: pytest
	coverage run --source=fundamentus -m \
	  pytest tests/ -v --color=yes --no-header --no-summary && \
	coverage report


test-detailed: ## - Test: pytest many details
	coverage run --source=fundamentus -m \
	  pytest tests/ -v --color=yes && \
	coverage report -m


test-silent: ##   - Test: pytest most silent
	pytest tests/ -q --color=yes --no-header --no-summary


test-bash:    ##    - Test: bash calling sample scripts
	LOGLEVEL=info /usr/bin/time ./tests/test-scripts.sh


data:	## - Save generated files to data/
	/bin/mv -f *.csv *xls? *ods ?.txt ??.txt ???.txt data/ || true


data-clean: ## - Clean data/
	/bin/rm -f data/*.*


pkg:	## - Package dist: create in dist/
	python setup.py sdist bdist_wheel

pkg-upload-test: ##  - PyPI: upload to Test
	twine upload --repository testpypi dist/*

pkg-upload-pypi: ##  - PyPI: upload to Test
	twine upload --repository pypi dist/*

