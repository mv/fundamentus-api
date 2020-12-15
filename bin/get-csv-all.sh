#!/bin/bash


dt=$( /bin/date '+%Y-%m-%d' )
file="bovespa-data.all.${dt}.csv"

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

##  1. Papel
##  2. Cotacao
##  3. P/L
##  4. P/VP
##  5. PSR
##  6. DY
##  7. P/Ativo
##  8. P/Cap.Giro
##  9. P/EBIT
## 10. P/ACL
## 11. EV/EBIT
## 12. EV/EBITDA
## 13. Mrg.Ebit
## 14. Mrg.Liq.
## 15. Liq.Corr.
## 16. ROIC
## 17. ROE
## 18. Liq.2meses

# awk: print header, sort the remainder, ';' as a separator
./fundamentus.py   \
  | egrep '^[A-Z]' \
  | awk -v OFS="; " \
        -v now="$(date +'%Y-%m-%d %X')" \
  '
    BEGIN {printf "Fundamentus; %s\n\n", now}
    NR==1 {printf "%-6s ;   %5s;   %-8s;  %-4s;   %6s;    %-3s;   %-9s;   %-5s;  %-7s;   %-8s;   %-8s;   %-5s;     %-5s;     %-8s;  %-11s;    %-4s;    %-4s;   %-8s\n", $1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15, $16, $17, $18 }
    NR>=2 {printf "%-6s ; %9.2f; %10.2f; %5.2f; %8.3f; %5.2f%%; %11.3f; %12.2f; %8.2f; %10.2f; %10.2f; %11.2f; %11.2f%%; %11.2f%%; %12.2f; %6.2f%%; %6.2f%%; %15.2f\n",
                     $1,     $2,     $3,    $4,    $5,  $6*100,     $7,     $8,    $9,    $10,    $11,    $12,  $13*100,  $14*100,    $15, $16*100, $17*100, $18   |"sort "}
  ' \
  > "${file}"

#                 Papel  Cotacao  p/l    p/vp , psr  , div.y  , p/at  , p/capg,p.ebit, p.circ,ev/ebit,ev/ebitda,mrg.ebit,mrg.lig,liq.corr,    roic,     roe, liq.2m

