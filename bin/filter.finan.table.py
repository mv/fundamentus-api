#!/usr/bin/env python3
#

# import set_path_fundamentus

from fundamentus import get_resultado
from fundamentus import print_table

from fundamentus import list_papel_setor


if __name__ == '__main__':

    data = get_resultado()

    # Filter by 'row'
    #   transpose 1: filter by row
    #   transpose 2: print by column
    setor = list_papel_setor(35)
    data2 = data.T[ setor ]
    data2 = data2.T

    print_table( data2.sort_index() )


