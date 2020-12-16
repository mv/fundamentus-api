#!/usr/bin/env python3

from fundamentus import get_fundamentus
from fundamentus import print_csv

from collections import OrderedDict

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
    data = OrderedDict(sorted(data.items()))

    # Reorder by column
#   data = OrderedDict(sorted(data.items(), key=lambda x: x[1]["DY"]))
#   data = OrderedDict(sorted(data.items(), key=lambda x: x[1]["ROE"]))

    print_csv(data)

