
"""
papel:
    Info from .../detalhes.php, i.e., with no parameters
"""

import requests
import requests_cache
import pandas   as pd
import time
import logging


def get_list_papel():
    """
    Papel: List of names only.

    Output:
      list
    """
    df  = get_df_papel()
    lst = list(df['Papel'])

    return lst


def get_df_papel():
    """
    Papel: Get list of names and descriptions
      URL:
        http://fundamentus.com.br/detalhes.php

    Output:
      df
    """

    url = 'http://fundamentus.com.br/detalhes.php'
    hdr = {'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',
           'Accept': 'text/html, text/plain, text/css, text/sgml, */*;q=0.01',
           'Accept-Encoding': 'gzip, deflate',
           }

    with requests_cache.enabled():
        content = requests.get(url, headers=hdr)

        if content.from_cache:
            logging.debug('.../detalhes.php: [CACHED]')
        else: # pragma: no cover
            logging.debug('.../detalhes.php: sleeping...')
            time.sleep(.500) # 500 ms


    ## parse
    df = pd.read_html(content.text)[0]

    return df


