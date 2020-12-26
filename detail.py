#!/usr/bin/env python3
#
#

from fundamentus import get_fundamentus
from fundamentus import print_csv

from fundamentus import get_details
from fundamentus import get_details_raw

from collections import OrderedDict
from tabulate    import tabulate


# %load_ext autoreload
# %autoreload

if __name__ == '__main__':

    papel = 'VALE3'

    lst = get_details_raw(papel)
#   print( tabulate(det[0]) )

    res = get_details(papel)
#   print( 'res: ', res)
    print( tabulate(res,headers=res.columns) )

    print("\n\n",res.columns)

