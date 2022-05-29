
"""
detalhes:
    Info from .../detalhes.php?papel=
"""

from . import utils

# import fundamentus.utils as utils

# from fundamentus.utils import dt_iso8601
# from fundamentus.utils import from_pt_br
# from fundamentus.utils import fmt_dec

import requests
import requests_cache
import pandas   as pd
import time
import logging, sys

from collections import OrderedDict


def get_fii(param):
    """
    Get detailed data from fundamentus:
      URL:
        http://fundamentus.com.br/detalhes.php?papel=WEGE3

    Input:
      - param: as str
        or
      - param: as list

    Output:
      - DataFrame
    """

    _type = str(type(param))
    logging.debug('[param] is of type [{}]'.format(_type))

    if _type == "<class 'list'>":
        logging.info('detalhes: call: get..._list()')
        return get_detalhes_fii_list(param)
    else:
        logging.info('detalhes: call: get..._fii()')
        return get_detalhes_fii(param)


def get_detalhes_fii_list(lst):
    """
    Get detailed data for a given list

    Input: list
    Output: DataFrame
    """

    result = pd.DataFrame()

    # build result for each get
    for fii in lst:
        logging.info('get list: [fii: {}]'.format(fii))
        df = get_detalhes_fii(fii)
        result = result.append(df)

    # duplicate column (fii is the index already)
    try:
        result.drop('FII', axis='columns', inplace=True)
    except: # pragma: no cover
        logging.error('drop column. Error=[{}].'.format(sys.exc_info()[1]))

    return result.sort_index()


def get_detalhes_fii(fii):
    """
    Get detailed data for a given 'fii'

    Input: str
    Output: DataFrame
    """

    ## raw
    logging.debug('1: get raw [{}]'.format(fii))
    tables = get_detalhes_fii_raw(fii)

    print(tables)
    if len(tables) == 6:
        pass
    else: # pragma: no cover
        logging.debug('HTML tables not rendered as expected. Len={}. Skipped.'.format(len(tables)))
        return None

    ## Build df by putting k/v together
    logging.debug('2: cleanup raw')
    keys = []
    vals = []

    ## Table 0
    ## 'top header/summary'
    df = tables[0]
    df[0] = utils.from_pt_br(df[0])
    df[2] = utils.from_pt_br(df[2])

    keys = keys + list(df[0]) # Summary: FII
    vals = vals + list(df[1])

    keys = keys + list(df[2]) # Summary: Cotacao
    vals = vals + list(df[3])

#   logging.debug('HTML table: 0. Done.')

    ## Table 1
    ## Valor de mercado
    df = tables[1]
    df[0] = utils.from_pt_br(df[0])
    df[2] = utils.from_pt_br(df[2])

    keys = keys + list(df[0])
    vals = vals + list(df[1])

    keys = keys + list(df[2])
    vals = vals + list(df[3])

#   logging.debug('HTML table: 1. Done.')

    ## Table 2
    ## 0/1: oscilacoes
    ## 2/3: indicadores
    df = tables[2].drop(0)      # remove extra header
    df[0] = utils.from_pt_br(df[0])
    df[2] = utils.from_pt_br(df[2])
    df[4] = utils.from_pt_br(df[4])

    df[0] = 'Oscilacao_' + df[0]  # more specific key name

    df[1] = utils.fmt_dec(df[1])    # oscilacoes
    df[3] = utils.fmt_dec(df[3])    # indicadores 1
    df[5] = utils.fmt_dec(df[5])    # indicadores 2

#   keys = keys + list(df[0]) # oscilacoes
#   vals = vals + list(df[1]) # OBS: ignoring for now...

    keys = keys + list(df[2]) # Indicadores 1
    vals = vals + list(df[3])

    keys = keys + list(df[4]) # Indicadores 2
    vals = vals + list(df[5])

#   logging.debug('HTML table: 2. Done.')

    ## Table 3
    ## balanco patrimonial
    df = tables[3].drop(0)    # remove extra line/header
    df[0] = utils.from_pt_br(df[0])
    df[2] = utils.from_pt_br(df[2])

    keys = keys + list(df[0])
    vals = vals + list(df[1])

    keys = keys + list(df[2])
    vals = vals + list(df[3])

#   logging.debug('HTML table: 3. Done.')

    ## Table 4
    ## DRE
    tables[4] = tables[4].drop(0)   # remove: line/header
    tables[4] = tables[4].drop(1)   # remove: 'Ultimos x meses'
    df = tables[4]
    df[0] = utils.from_pt_br(df[0])
    df[2] = utils.from_pt_br(df[2])

    df[0] = df[0] + '_12m'
    df[2] = df[2] + '_3m'

    keys = keys + list(df[0])
    vals = vals + list(df[1])

    keys = keys + list(df[2])
    vals = vals + list(df[3])

#   logging.debug('HTML table: 4. Done.')

    # hash to filter out NaN...
    hf = OrderedDict()
    for i, k in enumerate(keys):
        if pd.notna(k):
            hf[k] = vals[i]
        else: # pragma: no cover
            logging.debug('NaN. Skipped.')

    # Last fixes
    hf['Data_ult_cot']           = utils.dt_iso8601(hf['Data_ult_cot'])

    result = pd.DataFrame(hf, index=[fii])

    logging.debug('3: cleanup done')
    return result


def get_detalhes_fii_raw(fii='WEGE3'):
    """
    Get RAW detailed data from fundamentus:
      URL:
        http://fundamentus.com.br/detalhes.php?papel=WEGE3

    Output:
      list of df
    """

    ##
    ## Busca avançada por empresa
    ##
    url = 'http://fundamentus.com.br/detalhes.php?papel={}'.format(fii)
    hdr = {'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',
           'Accept': 'text/html, text/plain, text/css, text/sgml, */*;q=0.01',
           'Accept-Encoding': 'gzip, deflate',
           }

    with requests_cache.enabled():
        content = requests.get(url, headers=hdr)

        if content.from_cache:
            logging.debug('.../detalhes.php?papel={}: [CACHED]'.format(fii))
        else: # pragma: no cover
            logging.debug('.../detalhes.php?papel={}: sleeping...'.format(fii))
            time.sleep(.500) # 500 ms

    ## parse
    tables_html = pd.read_html(content.text, decimal=",", thousands='.')

    return tables_html
