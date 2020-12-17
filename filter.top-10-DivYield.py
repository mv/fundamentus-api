#!/usr/bin/env python3
#
# Ref:
#   https://stackoverflow.com/questions/38218501/python-get-top-n-keys-with-value-as-dictionary
#   https://stackoverflow.com/questions/30250715/how-do-you-get-the-first-3-elements-in-python-ordereddict/30250803
#   https://stackoverflow.com/questions/21062781/shortest-way-to-get-first-item-of-ordereddict-in-python-3
#

from fundamentus import get_fundamentus
from fundamentus import print_csv

from collections import OrderedDict


if __name__ == '__main__':

    # Parametros usados em 'Busca avancada por empresa'
    params = {'pl_min'          : '0.001',
              'divy_min'        : '0',
              'divy_max'        : '',
              }

    data = get_fundamentus(params)

    # Top 10:
    top_10 = OrderedDict(sorted(data.items(), key = lambda x: x[1]['DY'], reverse=True)[:10])

    print_csv(top_10)


    # Top 10
#   top_list = list(data)[:10]
#   top_data = OrderedDict()
#   for item in top_list: top_data[item] = data[item]

#   print_csv(top_data)


