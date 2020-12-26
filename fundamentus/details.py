#!/usr/bin/env python3
#
# Fundamentus v2.0
#   as a lib
#   2.0: pandas/DataFrame based
#

from fundamentus.utils import dt_iso8601
from fundamentus.utils import from_pt_br
from fundamentus.utils import fmt_dec

import requests
import requests_cache
import pandas   as pd

from collections import OrderedDict


def get_details_list(lst=[]):
    """
    Get detailed data for a given list
    """

    result = pd.DataFrame()

    for papel in lst:
        df = get_details(papel)
        result = result.append(df)

    result.drop('Papel', axis='columns', inplace=True)

    return result.sort_index()


def get_details(papel='WEGE3'):
    """
    Get detailed data from fundamentus:
      URL:
        http://fundamentus.com.br/detalhes.php?papel=WEGE3

    Output:
      df
    """

    ## raw
    df_list = get_details_raw(papel)

    ## Fix 0
    ## 'top header/summary'
    df = df_list[0]
    df[0] = from_pt_br( df[0] )
    df[2] = from_pt_br( df[2] )

    ## Fix 1
    ## Valor de mercado
    df = df_list[1]
    df[0] = from_pt_br( df[0] )
    df[2] = from_pt_br( df[2] )

    ## Fix 2
    ## 0/1: oscilacoes
    ## 2/3: indicadores
    df = df_list[2]
    df[0] = from_pt_br( df[0] )
    df[2] = from_pt_br( df[2] )
    df[4] = from_pt_br( df[4] )

    df[0] = 'Oscilacao_' + df[0]

    ## remove extra line
    df_list[2] = df_list[2].drop(0)

    ##
    fmt_dec(df_list[2], 1) # oscilacoes
    fmt_dec(df_list[2], 3) # indicadores
    fmt_dec(df_list[2], 5) # indicadores

    ## Fix 3
    ## balanco patrimonial
    df = df_list[3]
    df[0] = from_pt_br( df[0] )
    df[2] = from_pt_br( df[2] )

    ## remove extra line
    df_list[3] = df_list[3].drop(0)


    ## Fix 4
    ## DRE
    df = df_list[4]
    df[0] = from_pt_br( df[0] )
    df[2] = from_pt_br( df[2] )

    df[0] = df[0] + '_12m'
    df[2] = df[2] + '_3m'

    ## remove extra line
    df_list[4] = df_list[4].drop(0)
    df_list[4] = df_list[4].drop(1)

    keys = [] \
         + list(df_list[0][0]) \
         + list(df_list[0][2]) \
         + list(df_list[1][0]) \
         + list(df_list[1][2]) \
         + list(df_list[2][0]) \
         + list(df_list[2][2]) \
         + list(df_list[2][4]) \
         + list(df_list[3][0]) \
         + list(df_list[3][2]) \
         + list(df_list[4][0]) \
         + list(df_list[4][2])

    vals = [] \
         + list(df_list[0][1]) \
         + list(df_list[0][3]) \
         + list(df_list[1][1]) \
         + list(df_list[1][3]) \
         + list(df_list[2][1]) \
         + list(df_list[2][3]) \
         + list(df_list[2][5]) \
         + list(df_list[3][1]) \
         + list(df_list[3][3]) \
         + list(df_list[4][1]) \
         + list(df_list[4][3])

    result = OrderedDict()
    for i, k in enumerate(keys):
        if pd.isna(k):
            # print('NaN!')
            pass
        else:
            result[k] = vals[i]

    # Last fixes
    result['Data_ult_cot']           = dt_iso8601(result['Data_ult_cot'])
    result['Ult_balanco_processado'] = dt_iso8601(result['Ult_balanco_processado'])

    result = pd.DataFrame( result , index=[papel])

    ##
    return result


def get_details_raw(papel='WEGE3'):
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
    url = 'http://fundamentus.com.br/detalhes.php?papel={}'.format(papel)
    hdr = {'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',
           'Accept': 'text/html, text/plain, text/css, text/sgml, */*;q=0.01',
           'Accept-Encoding': 'gzip, deflate',
           }

    with requests_cache.enabled():
        content = requests.get(url, headers=hdr)

    ## parse
    df_list = pd.read_html(content.text, decimal=",", thousands='.')

    return df_list


## res:[
## df0
##            0                   1                2           3
## 0     ?Papel               VALE3         ?Cotação       87.36
## 1      ?Tipo               ON NM    ?Data últ cot  23/12/2020
## 2   ?Empresa          VALE ON NM      ?Min 52 sem       32.82
## 3     ?Setor           Mineração      ?Max 52 sem       87.80
## 4  ?Subsetor  Minerais Metálicos  ?Vol $ méd (2m)  2438780000,
##
## df1
##                    0             1                        2           3
## 0  ?Valor de mercado  461652000000  ?Últ balanço processado  30/09/2020
## 1    ?Valor da firma  496745000000              ?Nro. Ações  5284470000,
##
## df2
##              0           1                             2                             3                             4                             5
## 0   Oscilações  Oscilações  Indicadores fundamentalistas  Indicadores fundamentalistas  Indicadores fundamentalistas  Indicadores fundamentalistas
## 1          Dia       0,48%                          ?P/L                         29.82                          ?LPA                          2.93
## 2          Mês      12,00%                         ?P/VP                          2.37                          ?VPA                         36.83
## 3      30 dias      22,54%                       ?P/EBIT                          5.98                  ?Marg. Bruta                         46,7%
## 4     12 meses      70,03%                          ?PSR                          2.71                   ?Marg. EBIT                         45,3%
## 5         2020      70,30%                     ?P/Ativos                          1.02                ?Marg. Líquida                          7,3%
## 6         2019       6,85%                  ?P/Cap. Giro                         11.93                 ?EBIT / Ativo                         17,1%
## 7         2018      31,11%              ?P/Ativ Circ Liq                         -2.80                         ?ROIC                         20,1%
## 8         2017      62,56%                   ?Div. Yield                          4,4%                          ?ROE                          8,0%
## 9         2016      98,26%                  ?EV / EBITDA                          5.30                ?Liquidez Corr                          1.64
## 10        2015     -35,73%                    ?EV / EBIT                          6.43               ?Div Br/ Patrim                          0.44
## 11         NaN         NaN               ?Cres. Rec (5a)                         17,0%                  ?Giro Ativos                          0.38,
##
## df3
##                            0                          1                          2                          3
## 0  Dados Balanço Patrimonial  Dados Balanço Patrimonial  Dados Balanço Patrimonial  Dados Balanço Patrimonial
## 1                     ?Ativo               451140000000                ?Dív. Bruta                84982400000
## 2          ?Disponibilidades                49889400000              ?Dív. Líquida                35093000000
## 3          ?Ativo Circulante                98957100000               ?Patrim. Líq               194640000000,
##
## df4
##                                     0                                   1                                   2                                   3
## 0  Dados demonstrativos de resultados  Dados demonstrativos de resultados  Dados demonstrativos de resultados  Dados demonstrativos de resultados
## 1                    Últimos 12 meses                    Últimos 12 meses                     Últimos 3 meses                     Últimos 3 meses
## 2                    ?Receita Líquida                        170609000000                    ?Receita Líquida                         57905700000
## 3                               ?EBIT                         77219600000                               ?EBIT                         31328800000
## 4                      ?Lucro Líquido                         15480900000                      ?Lucro Líquido                         15615100000]
##
