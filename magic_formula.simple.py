#!/usr/bin/env python3

from fundamentus import get_fundamentus
from fundamentus import print_csv

from collections import OrderedDict

def print_simple(data):

     #         Papel   Cotacao P/L      EV/EBIT EV/EBITDA ROIC   ROE
    fmt_hdr = '{0:<6}; {1:<7}; {2:<10}; {3:<8}; {4:<10}; {5:<8}; {6:<8};'
    fmt_row = '{0:<6}; {1:>7}; {2:>10}; {3:>8}; {4:>10}; {5:>8}; {6:>8};'

    print(fmt_hdr.format('Papel',
                         'Cotacao',
                         'P/L',
                         'EV/EBIT',
                         'EV/EBITDA',
                         'ROIC',
                         'ROE'
                         ))

    for key, value in data.items():
        print(fmt_row.format(key,
                             value['Cotacao'],
                             value['P/L'],
                             value['EV/EBIT'],
                             value['EV/EBITDA'],
                             value['ROIC'],
                             value['ROE']
                             ))

def ranking(data):

    ##
#   data = OrderedDict(sorted(data.items(), key=lambda x: x[1]["ROE"]))

    return data



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

