#!/usr/bin/env python3
#
#

import set_path_fundamentus

from fundamentus import get_fii
from fundamentus import list_papel_all
from fundamentus import print_csv

from datetime import datetime, timedelta


if __name__ == '__main__':

    my_list = ["HGLG11"]

    df = get_fii(my_list[:10])

    # df.index.name = 'papel'

    # # skip older companies
    # dsince = datetime.today() - timedelta(days=10)
    # _since = dsince.strftime('%Y-%m-%d')

    # result = df[ df['Data_ult_cot'] > _since ]

    print(df)
    # today's csv
    # _today = datetime.today().strftime('%Y-%m-%d')
    # fname  = 'bovespa.detalhes.{}.csv'.format(_today)
    # result.to_csv(fname)

