#!/usr/bin/env python3
#

import pandas as pd

from fundamentus import get_fundamentus
from fundamentus import print_csv

from collections import OrderedDict

import time


def print_simple(data):
    """
    Print a 'simple' version of the CSV file that includes
      - Papel;Cotacao;P/L;EV/EBIT;EV/EBITDA;ROIC;ROE;'rankings'
      - rankings: EV/EBIT, ROIC, Magic ranking

      Input:
        OrderedDict()

      Output:
        stdout: CSV separated by ';'
    """

    #         Papel   Cotacao P/L      EV/EBIT EV/EBITDA ROIC    ROE #   r_EV     r_ROIC  r_magic
    fmt_hdr = '{0:<6}; {1:>7}; {2:>10}; {3:>8}; {4:>10}; {5:>8}; {6:>8}; {7:>12}; {8:>9}; {9:>10};'
    fmt_row = '{0:<6}; {1:>7}; {2:>10}; {3:>8.2f}; {4:>10.2f}; {5:>8.4f}; {6:>8.4f}; {7:>12}; {8:>9}; {9:>10};'

    print(fmt_hdr.format('Papel',
                         'Cotacao',
                         'P/L',
                         'EV/EBIT',
                         'EV/EBITDA',
                         'ROIC',
                         'ROE',
                         'rank_EV/EBIT',
                         'rank_ROIC',
                         'rank_Magic',
                         ))

    for key, value in data.items():
        print(fmt_row.format(key,
                             value['Cotacao'],
                             value['P/L'],
                             value['EV/EBIT'],
                             value['EV/EBITDA'],
                             value['ROIC'],
                             value['ROE'],
                             value['rank_EV/EBIT'],
                             value['rank_ROIC'],
                             value['rank_Magic'],
                             ))

    return


def filter_out(data):
    """
    filter out: Finance and Securities

    Input/Output: DataFrame()
    """

    # 35: Finance
    finan = get_fundamentus( { 'setor': '35' } ).keys()
    time.sleep(.2)

    # 38: Securities
    segur = get_fundamentus( { 'setor': '38' } ).keys()

    for key in (list(finan) + list(segur)):
        if key in data:
            del(data[key])

    return data


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
              'roe_min'       : '',
              'liq_min'       : '',
              'setor'         : '',
              }

    data = get_fundamentus(params)

    # my_columns = data.columns
    my_columns = ['cotacao', 'pl', 'evebit', 'evebitda', 'roic', 'roe']
    df = data[ my_columns ]


    # filter: list of finance companies: remove
#   df2 = filter_out(df)


    # Magic Formula: create rankings
    magic = ranking(df)
    print_table(magic)


#   from IPython import embed
#   embed()

