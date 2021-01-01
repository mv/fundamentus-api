#!/bin/bash

echodo() {
    echo "###"
    echo "### $@"
    echo "###"
    "$@" > /dev/null
    [ "$?" == 0 ] && (( exe_count = exe_count + 1))

    echo
    (( tot_count = tot_count + 1))
}

# debug level, if not set
export LOGLEVEL=${LOGLEVEL:-debug}

let exe_count=0
let tot_count=0

echodo python3 bin/detail.all.py
echodo python3 bin/detail.my-list.py
echodo python3 bin/detail.show.py
echodo python3 bin/filter.example.py
echodo python3 bin/filter.finan.csv.py
echodo python3 bin/filter.finan.table.py
echodo python3 bin/filter.top-10-DivYield.py
echodo python3 bin/fundamentus.csv.py
echodo python3 bin/magic_formula.simple.py

echo "==="
echo "=== Count: Success = ${exe_count}/${tot_count}"
echo "==="
echo

# Fail if all scripts failed
[ "${exe_count}" == 0 ] && exit 1

