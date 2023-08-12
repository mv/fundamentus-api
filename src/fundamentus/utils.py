
"""
utils:
    Utility helpers.
"""

import requests
import requests_cache
import pandas as pd
import logging

from tabulate import tabulate
from datetime import datetime
from dateutil.parser import parse
from pandas import Series


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


def fmt_dec(val: Series):
    """
    Fix percent:
      - replace string in pt-br
      - from '45,56%' to '45.56%'

    Input:
        Series, i.e., a DataFrame column
    """
    return pd.to_numeric(val.apply(parse_number_in_portuguese_locale))


def parse_number_in_portuguese_locale(no: str) -> float:
    """
    Parse numbers to float
    Percentages also will be parsed to float (3% to 3e-2)

    Input:
        A number string
    """
    try:
        no = no.replace('%', 'e-2').replace(".", "").replace(",", ".")
        return float(no)
    except:
        logging.error(f"Error: Unable to parse the number. {no}")
        return None

def perc_to_float(val: Series):
    """
    Percent to float
      - replace string in pt-br to float
      - from '45,56%' to 0.4556

    Input:
        Series
    """
    return fmt_dec(val)


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


