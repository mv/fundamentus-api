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

echodo python3 examples/detail.all.py
echodo python3 examples/detail.my-list.py
echodo python3 examples/detail.show.py
echodo python3 examples/filter.example.py
echodo python3 examples/filter.finan.csv.py
echodo python3 examples/filter.finan.table.py
echodo python3 examples/filter.top-10-DivYield.py
echodo python3 examples/fundamentus.csv.py
echodo python3 examples/magic_formula.simple.py

echo "==="
echo "=== Count: Success = ${exe_count}/${tot_count}"
echo "==="
echo

# Fail if all scripts failed
if [ "${exe_count}" -gt "0" ]
then exit 0
else exit 1  # fail
fi


