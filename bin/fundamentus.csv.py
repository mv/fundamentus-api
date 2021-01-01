#!/usr/bin/env python3
#
#

# import set_path_fundamentus

from fundamentus import get_resultado
from fundamentus import print_csv

if __name__ == '__main__':

    data = get_resultado()

    # Reorder by ticker
    data = data.sort_index(ascending=True)

    # filter on DataFrame
    data = data[ data.pl   > 0   ]
    data = data[ data.pl   < 100 ]
    data = data[ data.roe  > 0   ]
    data = data[ data.roic > 0   ]

    print_csv(data)

