#!/usr/bin/env python3

from fundamentus import get_fundamentus
from fundamentus import print_csv

from collections import OrderedDict


def print_simple(data):

    #         Papel   Cotacao P/L      EV/EBIT EV/EBITDA ROIC    ROE #   r_EV     r_ROIC  r_magic
    fmt_hdr = '{0:<6}; {1:<7}; {2:<10}; {3:<8}; {4:<10}; {5:<8}; {6:<8}; {7:<12}; {8:<9}; {9:<10};'
    fmt_row = '{0:<6}; {1:>7}; {2:>10}; {3:>8}; {4:>10}; {5:>8}; {6:>8}; {7:>12}; {8:>9}; {9:>10};'

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


def ranking(data):

    ## rank: EV/EBIT
    ##   in the book: rank by greater EBIT/EV
    ##   fundamentus: rank by smaller EV/EBIT **
    ##
    rank = OrderedDict(sorted(data.items(), key=lambda x: x[1]["EV/EBIT"]))

    idx = 1
    for key, value in rank.items():
        rank[key]['rank_EV/EBIT'] = idx
        idx += 1


    ## rank: ROIC
    ##   in the book: rank by greater Return on Invested Capital
    ##   fundamentus: rank by greater ROIC (best available aproximation) **
    ##
    rank = OrderedDict(sorted(data.items(), key=lambda x: x[1]["ROIC"], reverse=True))

    idx = 1
    for key, value in rank.items():
        rank[key]['rank_ROIC'] = idx
        idx += 1


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
              }

    data = get_fundamentus(params)

    # Magic Formula: create rankings
    magic = ranking(data)
    print_simple(magic)


