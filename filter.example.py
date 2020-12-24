#!/usr/bin/env python3
#
#

from fundamentus import get_fundamentus
from fundamentus import print_csv

if __name__ == '__main__':

    # Parametros usados em 'Busca avancada por empresa'
    params = {'pl_min'          : '0',
              'pl_max'          : '100',
              'roic_min'        : '0',
              'roic_max'        : '',
              'roe_min'         : '0',
              'roe_max'         : '',
              }

    data = get_fundamentus(params)

    # Reorder by ticker
    data.sort_values(by='papel', inplace=True)

    print_csv( data[ ['papel','cotacao','pl','dy','roic','roe'] ] )

