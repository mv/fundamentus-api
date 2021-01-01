#!/usr/bin/env python3
#

# import set_path_fundamentus

from fundamentus import get_resultado
from fundamentus import print_csv
from fundamentus import print_table


if __name__ == '__main__':

    data = get_resultado()

    # Top 10:
    data.sort_values( by='dy', inplace=True, ascending=False )
    top_10 = data[:10]

    print_csv(top_10)

