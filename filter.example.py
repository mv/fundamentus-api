#!/usr/bin/env python3
#
#

from fundamentus import get_fundamentus
from fundamentus import print_csv

if __name__ == '__main__':

    data = get_fundamentus()

    # Reorder by ticker
    data = data.sort_index(ascending=True)

    # filter on DataFrame
    data = data[ data.pl   > 0   ]
    data = data[ data.pl   < 100 ]
    data = data[ data.roe  > 0   ]
    data = data[ data.roic > 0   ]

    print_csv( data[ ['cotacao','pl','dy','roic','roe'] ] )

