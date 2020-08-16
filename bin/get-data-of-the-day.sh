#!/bin/bash


[ "$1" ] || {

  echo
  echo "  Usage: $0 -f"
  echo
  exit 1

}

dt=$( /bin/date '+%Y-%m-%d' )
file="data/fundamentus.${dt}.txt"

echo "Generating: [$file]"

# awk: print 1st line, sort the remainder
./fundamentus.py | egrep '^[A-Z]' | awk 'NR<2 {print $0; next} {print $0 | "sort "}' > "${file}"



