#!/bin/bash


dt=$( /bin/date '+%Y-%m-%d' )
file="magic-formula.simple.${dt}.csv"

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
echo

##  1. Papel         **
##  2. Cotacao       **
##  3. P/L           *
##  4. EV/EBIT       *
##  5. EV/EBITDA     *
##  6. ROIC          *
##  7. ROE           *
##  8. rank_pl
##  9. rank_ebitda
## 10. rank_roe

# awk: print header, sort the remainder, ';' as a separator
cat s1.txt \
  | awk -F';' '
    ##
    ## Filters
    ##
    /^Papel/    {printf "%s\n", $0 }
    /^[A-Z]{3}/ {if ($3 > 0 && $4 > 0 && $5 > 0 && $6 > 0 && $7 > 0) printf "%s\n", $0 }
  ' \
  \
  | awk -F';' '
    ##
    ## PL
    ##
    /^Papel/    {printf "%s\n", $0 }
    /^[A-Z]{3}/ {printf "%s\n", $0 | "sort -n -k3 -t\";\"" } ' \
  | awk -F';' '
    /^Papel/    {printf "%s ; Rank_PL\n", $0 }
    /^[A-Z]{3}/ {printf "%s ;     %3d\n", $0 , NR-1}
  ' \
  | awk -F';' '
    ##
    ## EV/Ebitda
    ##
    /^Papel/    {printf "%s\n", $0 }
    /^[A-Z]{3}/ {printf "%s\n", $0 | "sort -n -k5 -t\";\"" } ' \
  | awk -F';' '
    /^Papel/    {printf "%s ; Rank_EV_Ebtida\n", $0 }
    /^[A-Z]{3}/ {printf "%s ;            %3d\n", $0 , NR-1}
  ' \
  | awk -F';' '
    ##
    ## ROE
    ##
    /^Papel/    {printf "%s\n", $0 }
    /^[A-Z]{3}/ {printf "%s\n", $0 | "sort -r -n -k6 -t\";\" -t\"%\" " } ' \
  | awk -F';' '
    /^Papel/    {printf "%s ; Rank_ROE\n", $0 }
    /^[A-Z]{3}/ {printf "%s ;      %3d\n", $0 , NR-1}
  ' \
  | awk -F';' '
    ##
    ## Sum of rankings: Magic Formula
    ##
    /^Papel/    {printf "%s ; Magic\n", $0 }
    /^[A-Z]{3}/ {printf "%s ;   %3d\n", $0 , ($8+$9)}
  ' \
  | awk -F';' '
    ##
    ## Sum of rankings: extra: Mv
    ##
    /^Papel/    {printf "%s ;    Mv\n", $0 }
    /^[A-Z]{3}/ {printf "%s ;   %3d\n", $0 , ($8+$9+$10)}
  ' \
  | awk -F';' '
    ##
    ## Last sort
    ##
    /^Papel/    {printf "%s\n", $0 }
    /^[A-Z]{3}/ {printf "%s\n", $0 | "sort -n -k11 -t\";\"" }
  ' \
  > "${file}"

#   /^Papel/    {printf "%s ; rank\n", $0 }
#   /^[A-Z]{3}/ {printf "%s ; %3d\n" , $0 , NR-3}
#   NR==1 {printf "%-6s ;    %7s ;    %7s ;    %7s ;    %9s ;     %4s ; %8s\n"   , $1, $2, $3, $11, $12, $17, $16 }
#   NR>=2 {printf "%-6s ; %10.2f ; %10.2f ; %10.2f ; %12.2f ; %7.2f%% ; %7.2f%%\n", $1, $2, $3, $11, $12, $17*100, $16*100 | "sort "}
#   BEGIN {printf ";Magic Formula;Fundamentus; %s\n\n", now}

