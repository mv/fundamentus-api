#!/usr/bin/env python3

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
    filter out: finance and Securities

    Input/Output: OrderedDict()
    """

    # 35: Finance
    finan = get_fundamentus( { 'setor': '35' } ).keys()
    time.sleep(.2)

    # 38: Securities
    segur = get_fundamentus( { 'setor': '38' } ).keys()

    lst = list(finan) + list(segur)
    for key in lst:
        if key in data:
            del(data[key])

    return data


def ranking(data):
    """
    Ranking:
      Order data by EV/EBIT first, and ROIC next

      Input:
        OrderedDict()

      Return:
        OrderedDict()

      Obs:
        rank: EV/EBIT
          in the book: rank by greater EBIT/EV
          fundamentus: rank by smaller EV/EBIT **

        rank: ROIC
          in the book: rank by greater Return on Invested Capital
          fundamentus: rank by greater ROIC (best available aproximation) **
    """

    ## rank: EV/EBIT
    rank = OrderedDict(sorted(data.items(), key=lambda x: x[1]["EV/EBIT"]))

    # keys() are sorted because 'OrderedDict' keeps its order ;D
    for i, key in enumerate(rank.keys()):
        rank[key]['rank_EV/EBIT'] = i+1


    ## rank: ROIC
    rank = OrderedDict(sorted(data.items(), key=lambda x: x[1]["ROIC"], reverse=True))

    for i, key, in enumerate(rank.keys()):
        rank[key]['rank_ROIC'] = i+1


    ## Magic Formula...
    for key, value in rank.items():
        magic = rank[key]['rank_EV/EBIT'] + \
                rank[key]['rank_ROIC']
        rank[key]['rank_Magic'] = magic


    rank = OrderedDict(sorted(data.items(), key=lambda x: x[1]["rank_Magic"]))

    return rank


if __name__ == '__main__':

    # Parametros usados em 'Busca avancada por empresa'
    params = {'pl_min'        : '0',
              'firma_ebit_min': '0.001',
              'roic_min'      : '0.001',
              'roe_min'       : '',
              'liq_min'       : '1000000',
              'setor'         : '',
              }

    data = get_fundamentus(params)


    # remove: list of finance companies
    data2 = filter_out(data)


    # Magic Formula: create rankings
    magic = ranking(data2)
    print_simple(magic)

#   from IPython import embed
#   embed()

