#!/usr/bin/env python3
#

from fundamentus import get_resultado
from fundamentus import print_csv


if __name__ == '__main__':

    # Parametros usados em 'Busca avancada por empresa'
    params = {'pl_min'  : '',
              'pl_max'  : '',
              'roic_min': '',
              'roic_max': '',
              'roe_min' : '',
              'roe_max' : '',
              }

#   data = get_resultado(params)
    data = get_resultado()

    # Reorder by ticker
    print_csv( data.sort_values(by='Papel') )


