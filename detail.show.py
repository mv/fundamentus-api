#!/usr/bin/env python3
#
#

from fundamentus import get_detalhes
from fundamentus import get_detalhes_raw

from fundamentus import print_csv
from tabulate    import tabulate


if __name__ == '__main__':

    papel = 'VALE3'

    raw = get_detalhes_raw(papel)
    print("\n\nDetalhes: RAW\n")
    print(raw)


    det = get_detalhes(papel)
    print("\n\nDetalhes: transposed\n")
    print(det.T,"\n")


