
"""
utils:
    Utility helpers.
"""

import requests
import requests_cache
import pandas   as pd
import logging

from tabulate import tabulate
from datetime import datetime
from dateutil.parser import parse


def dt_iso8601(val):
    """
    Format dates to yyyy-mm-dd
    Input:
        scalar
    """
    try:
        dt = parse(val, dayfirst=True).strftime('%Y-%m-%d')
        return dt
    except:
        logging.debug('Error...')
        return



def from_pt_br(val):
    """
    from_pt_br: fix key/label by removing pt-br stuff
    Input:
        DataFrame()
    """
    res = val
    res = res.str.strip('?')
    res = res.str.replace('(','')
    res = res.str.replace(')','')
    res = res.str.replace('$','')
    res = res.str.replace('.','')
    res = res.str.replace('/','')
    res = res.str.replace('ç','c')
    res = res.str.replace('ã','a')
    res = res.str.replace('é','e')
    res = res.str.replace('ê','e')
    res = res.str.replace('ó','o')
    res = res.str.replace('õ','o')
    res = res.str.replace('í','i')
    res = res.str.replace('ú','u')
    res = res.str.replace('Ú','U')
    res = res.str.replace(' ','_')
    res = res.str.replace('__','_')

    return res


def fmt_dec(val):
    """
    Fix percent:
      - replace string in pt-br
      - from '45,56%' to '45.56%'

    Input:
        DataFrame
    """

    res = val
    res = res.str.replace('.', '' )
    res = res.str.replace(',', '.')
#   res = res.astype(float)
#   res = res.astype(float) / 100
#   res = '{:4.2f}%'.format(res)

    return res


def perc_to_float(val):
    """
    Percent to float
      - replace string in pt-br to float
      - from '45,56%' to 0.4556

    Input:
        (DataFrame, column_name)
    """

    res = val
    res = res.str.rstrip('%')
    res = res.str.replace('.', '' )
    res = res.str.replace(',', '.')
    res = res.astype(float) / 100

    return res


def print_csv(data):
    """
    CSV printed to stdout
    """
    print(data.to_csv( index=True
                     , header=True
                     , decimal='.'
                     , float_format='%.4f'
                     )
         )

    return


def print_table(data):
    """
    Text table printed to stdout
      - separator: '|'
      - fixed-width columns for better reading
    """
    print( tabulate ( data
                    , headers=data.columns
                    , tablefmt='presto'
                    , floatfmt=".4f"
                    , disable_numparse=False
               )
     )

    return


