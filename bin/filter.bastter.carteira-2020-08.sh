#!/bin/bash


[ "$1" ] || {

  echo
  echo "  Usage: $0 <data-file>"
  echo
  exit 1

}

data="$1"

dt=$( /bin/date '+%Y-%m-%d' )
file="data/bastter.filter.${dt}.csv"
tmpfile="/tmp/fundamentus.$$"

filter='ABEV|ARZZ|B3SA|BBAS|BBDC|BBSE|CARD|EGIE|ENAT|ENBR|EQTL|EZTC|FLRY|GRND|GUAR|HGTX|HYPE|ITSA|LCAM|LEVE|LREN|MDIA|MGLU|NTCO|ODPV|PRIO|PSSA|RADL|SHUL|TAEE|WEGE|YDUQ'
filter='ABEV|B3SA|BBAS|BBDC|BBSE|CARD|EGIE|ENAT|ENBR|EQTL|EZTC|FLRY|GRND|GUAR|HGTX|HYPE|ITSA|LCAM|LEVE|LREN|MDIA|ODPV|PRIO|PSSA|RADL|SHUL|TAEE|WEGE|YDUQ'


echo "Generating: [$file]"

# Preserve header
head -1 "${data}" > "${tmpfile}"

# Filter list
egrep ${filter} "${data}" >> "${tmpfile}"

# Filter: Papel,Cotacao,P/L,ROE,ROIC
awk '{print $1,$2,$3,$17,$16}' "${tmpfile}" \
  | column -t  \
  > "${file}"


/bin/rm -f "${tmpfile}"

