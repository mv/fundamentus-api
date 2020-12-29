#!/bin/bash
#
# Remember: setup virtualenv
#   $ pip3 install virtualenv
#
# Ref:
#   https://docs.python-guide.org/dev/virtualenvs/
#

echodo() {
    echo "###"
    echo "### $@"
    echo "###"
    "$@"
}

echodo virtualenv venv
echodo source venv/bin/activate
echodo pip install -r required.txt

