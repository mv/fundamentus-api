#!/usr/bin/env python3
#

from fundamentus import get_fundamentus
from fundamentus import print_csv
from fundamentus import print_table


if __name__ == '__main__':

    data = get_fundamentus()

    # Top 10:
    data.sort_values( by='dy', inplace=True, ascending=False )
    top_10 = data[:10]

    print_csv(top_10)

