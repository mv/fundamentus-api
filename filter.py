#!/usr/bin/env python3

from fundamentus import get_fundamentus
from fundamentus import print_csv


if __name__ == '__main__':

    # Parametros usados em 'Busca avancada por empresa'
    params = {'pl_min'          : '0',
              'pl_max'          : '80',
              'pvp_min'         : '',
              'pvp_max'         : '',
              'roic_in'         : '0',
              'roic_max'        : '',
              'roe_min'         : '0',
              'roe_max'         : '',
              'setor'           : '',
              }

    data = get_fundamentus(params)
    print_csv(data)

