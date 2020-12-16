#!/bin/bash


dt=$( /bin/date '+%Y-%m-%d' )
file="bovespa-data.simple.${dt}.csv"

usage() {
  echo
  echo "  Usage: $0 -f [filename]"
  echo
  echo "    -f: filename. Default: $file"
  echo
  exit 1
}

if [ "$1" != "-f" ]
then usage
else
  if [ "$2" != "" ]
  then file="$2"
  fi
fi

echo "Generating: [$file]"

##  1. Papel         **
##  2. Cotacao       **
##  3. P/L           *
##  4. P/VP
##  5. PSR
##  6. DY
##  7. P/Ativo
##  8. P/Cap.Giro
##  9. P/EBIT
## 10. P/ACL
## 11. EV/EBIT       *
## 12. EV/EBITDA     *
## 13. Mrg.Ebit
## 14. Mrg.Liq.
## 15. Liq.Corr.
## 16. ROIC          *
## 17. ROE           *
## 18. Liq.2meses

# awk: print header, sort the remainder, ';' as a separator
./fundamentus.py   \
  | egrep '^[A-Z]' \
  | awk -v now="$(date +'%Y-%m-%d %X')" \
  '
    BEGIN {printf ";Fundamentus; %s\n\n", now}
    NR==1 {printf "%-6s ;    %7s ;    %7s ;    %7s ;    %9s ;   %5s ;   %5s\n"   , $1, $2, $3, $11, $12, $17, $16 }
    NR>=2 {printf "%-6s ; %10.2f ; %10.2f ; %10.2f ; %12.2f ; %7.4f ; %7.4f\n", $1, $2, $3, $11, $12, $17, $16 | "sort "}
  ' \
  > "${file}"

#   NR>=2 {printf "%-6s ; %10.2f ; %10.2f ; %10.2f ; %12.2f ; %7.2f%% ; %7.2f%%\n", $1, $2, $3, $11, $12, $17*100, $16*100 | "sort "}

