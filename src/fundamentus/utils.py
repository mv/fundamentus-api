
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


#
# Ref:
#   https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.replace.html
#   https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.replace.html
#


def dt_iso8601(val):
    """
    Format dates to yyyy-mm-dd
    Input:
        scalar
    """
    try:
        dt = parse(val, dayfirst=True).strftime('%Y-%m-%d')
        return dt
    except: # pragma: no cover
        logging.debug('Error...')
        return



def from_pt_br(val):
    """
    from_pt_br: fix key/label by removing pt-br stuff
    Input:
        Series, i.e., a DataFrame column
    """
    res = val

    res.replace( to_replace=r'[?]'  , value=''  , regex=True, inplace=True )
    res.replace( to_replace=r'[(]'  , value=''  , regex=True, inplace=True )
    res.replace( to_replace=r'[)]'  , value=''  , regex=True, inplace=True )
    res.replace( to_replace=r'[$]'  , value=''  , regex=True, inplace=True )
    res.replace( to_replace=r'[.]'  , value=''  , regex=True, inplace=True )
    res.replace( to_replace=r'[/]'  , value=''  , regex=True, inplace=True )

    res.replace( to_replace=r'[ç]'  , value='c' , regex=True, inplace=True )
    res.replace( to_replace=r'[âáã]', value='a' , regex=True, inplace=True )
    res.replace( to_replace=r'[ôóõ]', value='o' , regex=True, inplace=True )
    res.replace( to_replace=r'[êé]' , value='e' , regex=True, inplace=True )
    res.replace( to_replace=r'[îí]' , value='i' , regex=True, inplace=True )
    res.replace( to_replace=r'[ûú]' , value='u' , regex=True, inplace=True )
    res.replace( to_replace=r'[ÛÚ]' , value='U' , regex=True, inplace=True )

    res.replace( to_replace=r'[ ]'  , value='_' , regex=True, inplace=True )
    res.replace( to_replace=r'__'   , value='_' , regex=True, inplace=True )

    return res


def fmt_dec(val):
    """
    Fix percent:
      - replace string in pt-br
      - from '45,56%' to '45.56%'

    Input:
        Series, i.e., a DataFrame column
    """

    res = val
    res = res.replace( to_replace=r'[.]', value='' , regex=True )
    res = res.replace( to_replace=r'[,]', value='.', regex=True )
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
    res = res.replace( to_replace=r'[%]', value='' , regex=True )
    res = res.replace( to_replace=r'[.]', value='' , regex=True )
    res = res.replace( to_replace=r'[,]', value='.', regex=True )
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


