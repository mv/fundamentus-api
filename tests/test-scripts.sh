#!/bin/bash

echodo() {
    echo "###"
    echo "### $@"
    echo "###"
    "$@" > /dev/null
    echo
}

export LOGLEVEL=debug

echodo python3 bin/detail.all.py
echodo python3 bin/detail.my-list.py
echodo python3 bin/detail.show.py
echodo python3 bin/filter.example.py
echodo python3 bin/filter.finan.csv.py
echodo python3 bin/filter.finan.table.py
echodo python3 bin/filter.top-10-DivYield.py
echodo python3 bin/fundamentus.csv.py
echodo python3 bin/magic_formula.simple.py

