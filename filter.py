#!/usr/bin/env python3

from fundamentus import get_fundamentus
from fundamentus import print_csv


if __name__ == '__main__':

    # Parametros usados em 'Busca avancada por empresa'
    params = {'pl_min'          : '',
              'pl_max'          : '',
              'pvp_min'         : '',
              'pvp_max'         : '',
              'roic_min'        : '0',
              'roic_max'        : '',
              'roe_min'         : '',
              'roe_max'         : '',
              'setor'           : '',
              }

    data = get_fundamentus(params)
    print_csv(data)

