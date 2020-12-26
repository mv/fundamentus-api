#!/usr/bin/env python3
#
#

from fundamentus import get_details
from fundamentus import get_details_raw

from fundamentus import print_csv
from tabulate    import tabulate


if __name__ == '__main__':

    papel = 'VALE3'

    raw = get_details_raw(papel)
    print("\n\nDetails: RAW\n")
    print(raw)


    det = get_details(papel)
    print("\n\nDetails: transposed\n")
    print(det.T,"\n")


