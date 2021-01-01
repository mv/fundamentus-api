#!/usr/bin/env python3
#

# import set_path_fundamentus

import pandas as pd

from fundamentus import get_resultado
from fundamentus import get_setor_id
from fundamentus import list_papel_setor

from fundamentus import print_csv
from fundamentus import print_table

import time


def filter_out(data):
    """
    filter out: Finance and Securities

    Input/Output: DataFrame()
    """

    df = data
    lst = []
    lst = lst + list_papel_setor( get_setor_id('financeiro') )
    lst = lst + list_papel_setor( get_setor_id('seguros'   ) )

    for idx in lst:
        try:
            df = df.drop(idx)
            # print('idx: ',idx, 'dropped.')
        except:
            # print('idx: ',idx, 'NOT FOUND.')
            pass

    return df


def ranking(data):
    """
    Ranking:
      Order data by EV/EBIT first, and ROIC next

      Input/Output: DataFrame()

      Obs:
        rank: EV/EBIT
          in the book: rank by greater EBIT/EV
          fundamentus: rank by smaller EV/EBIT **

        rank: ROIC
          in the book: rank by greater Return on Invested Capital
          fundamentus: rank by greater ROIC (best available aproximation) **
    """

    magic = data


    ## rank: EV/EBIT
    rank1 = data.sort_values('evebit', ascending=True).index

    df1 = pd.DataFrame( { 'rank': range(len(data)) }, index = rank1)
    df1 += 1
    magic = magic.assign(rank_evebit = df1)


    ## rank: ROIC
    rank2 = data.sort_values('roic', ascending=False).index

    df2 = pd.DataFrame({ 'rank': range( len(data) )}, index = rank2)
    df2 += 1
    magic = magic.assign(rank_roic = df2)


    ## Magic Formula...
    magic['rank_magic'] = magic['rank_evebit'] + magic['rank_roic']
    magic = magic.sort_values('rank_magic')


    return magic


if __name__ == '__main__':

    # GET: all dataset (cacheable)
    data = get_resultado()

    # filters
    data2 = data
    data2 = data2[ data2.pl       > 0  ]
    data2 = data2[ data2.pl       < 30 ]
    data2 = data2[ data2.roic     > 0  ]
    data2 = data2[ data2.roe      > 0  ]
    data2 = data2[ data2.evebit   > 0  ]
    data2 = data2[ data2.evebitda > 0  ]
    data2 = data2[ data2.divbpatr < 3  ]
    data2 = data2[ data2.liq2m    > 0  ]
    data2 = data2[ data2.c5y      > 0  ]
    data2 = data2[ data2.pacl     > 0  ]

#   my_columns = data.columns
#   my_columns = ['cotacao', 'pl', 'pvp', 'psr', 'dy', 'pa', 'pcg', 'pebit', 'pacl',
#                 'evebit', 'evebitda', 'mrgebit', 'mrgliq', 'roic', 'roe',
#                 'liqc', 'liq2m', 'patrliq', 'divbpatr', 'c5y']
    my_columns = ['pl', 'pvp', 'psr', 'dy', 'pa', 'pcg', 'pebit', 'pacl',
                  'evebit', 'evebitda', 'mrgebit', 'mrgliq', 'roic', 'roe',
                  'liqc', 'divbpatr', 'c5y']
    df1 = data2[ my_columns ]


    # filter: list of finance companies: remove
    df2 = filter_out(df1)


    # Magic Formula: create rankings
    magic = ranking(df2)
    print_csv(magic)


