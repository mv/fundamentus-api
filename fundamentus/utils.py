#!/usr/bin/env python3
#
# Fundamentus v2.0
#   as a lib
#   2.0: pandas/DataFrame based
#

import requests
import requests_cache
import pandas   as pd

from tabulate import tabulate
from datetime import datetime


def dt_iso8601(val):
    """
    Format dates: yyyy-mm-dd
    """
    dt = datetime.strptime(val, '%d/%m/%Y')
    dt = datetime.strftime(dt , '%Y-%m-%d')

    return dt


def from_pt_br(val):
    """
    from_pt_br: fix key/label by removing pt-br stuff
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

    Input: DataFrame, column_name
    """

    res = val
    res = res.str.replace('.', '' )
    res = res.str.replace(',', '.')
#   res = res.astype(float)
#   res = res.astype(float) / 100
#   res = '{:4.2f}%'.format(res)

    return res


def perc_to_float(df, column):
    """
    Percent to float
      - df inplace: replace string in pt-br
      - from '45,56%' to '0.4556'

    Input: DataFrame, column_name
    """

    df[column] = df[column].str.rstrip('%')
    df[column] = df[column].str.replace('.', '' )
    df[column] = df[column].str.replace(',', '.')
    df[column] = df[column].astype(float) / 100

    return


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


