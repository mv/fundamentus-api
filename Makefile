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
_python_verson := 3.7.4

# My vars: recursive

_dt = $(warning 'Invoking shell')$(shell date +%Y-%m-%d.%H:%M:%S)


###
### targets/tasks
###
.DEFAULT_GOAL:= help
.PHONY: help show init clean pip pip-dev venv venv-clean venv-clear pyenv data data-clean

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
	@echo "  Python Version: [$(_python_verson)]"
	@echo


init:   ## - Virtualenv install + pip install
init:   venv pip


venv:   ## - Create virtualenv
	pip3 install virtualenv
	virtualenv $(_venv)

venv-clear: ## - Reinstall virtualenv (--clear)
	@echo "Reinstalling..."
	virtualenv $(_venv) --clear

venv-clean: ## - Clean: rm virtualenv
	/bin/rm -rf $(_venv)


pip:    ## - Pip install from requirements*.txt
	. $(_venv)/bin/activate              && \
	pip3 install -r requirements.txt


pip-dev: ## - Pip install from requirements*.txt
	. $(_venv)/bin/activate              && \
	pip3 install -r requirements-dev.txt


pyenv:  ## - Pyenv Install + set local
	@pyenv install $(_python_verson) || :
	@pyenv local   $(_python_verson)
	@pyenv version


clean:	## - Cleanup: pycache stuff
	find . -type d -name __py*cache__ -exec rm -rf {} \; 2>/dev/null
	find . -type f | egrep -i '.pyc|.pyb' | xargs rm
	rm -rf .pytest_cache
	rm -rf .ipynb_checkpoints


test:	## - Test: py.test -v
	@if [ -f $(_config_default) ]; \
	then   . $(_config_default) && pytest -v -s tests/ ; \
	else echo "Error: must define env vars in $(_config_default)"  ; \
	fi

tst:	## - Test: using nose
	nosetests tests


data:	## - Save generated files to data/
	/bin/mv -f *.csv *xls? *ods ?.txt ??.txt ???.txt data/ || true


data-clean: ## - Clean data/
	/bin/rm -f data/*.*

