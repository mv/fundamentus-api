#!/usr/bin/env python3

from fundamentus import get_fundamentus
from fundamentus import print_csv

from collections import OrderedDict


def print_simple(data):

    #         Papel   Cotacao P/L      EV/EBIT EV/EBITDA ROIC    ROE #   r..EV    r..ROE  r..ROIC magic
    fmt_hdr = '{0:<6}; {1:<7}; {2:<10}; {3:<8}; {4:<10}; {5:<8}; {6:<8}; {7:<14}; {8:<8}; {9:<9}; {10:<5};'
    fmt_row = '{0:<6}; {1:>7}; {2:>10}; {3:>8}; {4:>10}; {5:>8}; {6:>8}; {7:>14}; {8:>8}; {9:>9}; {10:>5};'

    print(fmt_hdr.format('Papel',
                         'Cotacao',
                         'P/L',
                         'EV/EBIT',
                         'EV/EBITDA',
                         'ROIC',
                         'ROE',
                         'rank_EV/EBITDA',
                         'rank_ROE',
                         'rank_ROIC',
                         'Magic',
                         ))

    for key, value in data.items():
        print(fmt_row.format(key,
                             value['Cotacao'],
                             value['P/L'],
                             value['EV/EBIT'],
                             value['EV/EBITDA'],
                             value['ROIC'],
                             value['ROE'],
                             value['rank_EV/EBITDA'],
                             value['rank_ROE'],
                             value['rank_ROIC'],
                             value['Magic'],
                             ))

    return

def ranking(data):

    ## rank: EV/EBITDA
    rank = OrderedDict(sorted(data.items(), key=lambda x: x[1]["EV/EBITDA"]))

    idx = 1
    for key, value in rank.items():
        rank[key]['rank_EV/EBITDA'] = idx
        idx += 1


    ## rank: ROE
    rank = OrderedDict(sorted(data.items(), key=lambda x: x[1]["ROE"]))

    idx = 1
    for key, value in rank.items():
        rank[key]['rank_ROE'] = idx
        idx += 1


    ## rank: ROIC
    rank = OrderedDict(sorted(data.items(), key=lambda x: x[1]["ROIC"]))

    idx = 1
    for key, value in rank.items():
        rank[key]['rank_ROIC'] = idx
        idx += 1


    ## Magic Formula...
    for key, value in rank.items():
        magic = rank[key]['rank_EV/EBITDA'] + \
                rank[key]['rank_ROE']
        rank[key]['Magic'] = magic


    rank = OrderedDict(sorted(data.items(), key=lambda x: x[1]["Magic"]))
    return rank



if __name__ == '__main__':

    # Parametros usados em 'Busca avancada por empresa'
    params = {'pl_min'   : '0',
              'pl_max'   : '100',
              'roic_min' : '0',
              'roe_min'  : '.6',
              }

    data = get_fundamentus(params)

    # Magic Formula: create rankings
    magic = ranking(data)
    print_simple(magic)


