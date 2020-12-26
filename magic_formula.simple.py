#!/usr/bin/env python3
#

import pandas as pd

from fundamentus import get_fundamentus
from fundamentus import get_setor_data
from fundamentus import get_setor_id
from fundamentus import list_setor
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
    lst = lst + get_setor_data( get_setor_id('financeiro') )
    lst = lst + get_setor_data( get_setor_id('seguros'   ) )

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

    # Parametros usados em 'Busca avancada por empresa'
    params = {'pl_min'        : '0',
              'firma_ebit_min': '0.001',
              'roic_min'      : '0.001',
              'roe_min'       : '0.001',
              'liq_min'       : '',
              'setor'         : '',
              }

    data = get_fundamentus(params)

    # my_columns = data.columns
    my_columns = ['cotacao', 'pl', 'evebit', 'evebitda', 'roic', 'roe']
    df = data[ my_columns ]


    # filter: list of finance companies: remove
    df2 = filter_out(df)


    # Magic Formula: create rankings
    magic = ranking(df2)
    print_table(magic)


#   from IPython import embed
#   embed()

#   id_fin = get_setor_id('financeiro')
#   id_seg = get_setor_id('seguros'   )

#   idx_fin = get_setor_data( get_setor_id('financeiro') )
#   idx_seg = get_setor_data( get_setor_id('seguros'   ) )

