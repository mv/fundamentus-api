#!/usr/bin/env python3

import requests
import pandas   as pd

from collections import OrderedDict
from decimal     import Decimal


# URL:
#   http://fundamentus.com.br/buscaavancada.php
#   http://fundamentus.com.br/resultado.php

def get_fundamentus(filters={}, *args, **kwargs):

    ## Parametros usados em 'Busca avancada por empresa'
    ##   Default: todas as empresas
    ##   Detalhes: view-source:http://fundamentus.com.br/buscaavancada.php
    ##
    params = {'pl_min'          : '', 'pl_max'          : '',
              'pvp_min'         : '', 'pvp_max'         : '',
              'psr_min'         : '', 'psr_max'         : '',
              'divy_min'        : '', 'divy_max'        : '',
              'pativos_min'     : '', 'pativos_max'     : '',
              'pcapgiro_min'    : '', 'pcapgiro_max'    : '',
              'pebit_min'       : '', 'pebit_max'       : '',
              'fgrah_min'       : '', 'fgrah_max'       : '',
              'firma_ebit_min'  : '', 'firma_ebit_max'  : '',
              'firma_ebitda_min': '', 'firma_ebitda_max': '',
              'margemebit_min'  : '', 'margemebit_max'  : '',
              'margemliq_min'   : '', 'margemliq_max'   : '',
              'liqcorr_min'     : '', 'liqcorr_max'     : '',
              'roic_min'        : '', 'roic_max'        : '',
              'roe_min'         : '', 'roe_max'         : '',
              'liq_min'         : '', 'liq_max'         : '',
              'patrim_min'      : '', 'patrim_max'      : '',
              'divbruta_min'    : '', 'divbruta_max'    : '',
              'tx_cresc_rec_min': '', 'tx_cresc_rec_max': '',
              'setor'           : '',
              }

    ## Parametros: aplicando 'meus' filtros
    ##
    params.update(filters)


    ##
    ## Busca avançada por empresa
    ##

    url = 'http://www.fundamentus.com.br/resultado.php'

    hdr = {'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',
           'Accept': 'text/html, text/plain, text/css, text/sgml, */*;q=0.01',
           'Accept-Encoding': 'gzip, deflate',
           }

    content = requests.post(url, headers=hdr, data=params).text

    # parse
    df = pd.read_html(content, decimal=",", thousands='.')[0]

    # load
    results = OrderedDict()

    for row in df.to_dict('records'):
        results[row['Papel']] = {
            # fix header names
            'Papel'         :          row['Papel'            ] ,
            'Cotacao'       :          row['Cotação'          ] ,
            'P/L'           :          row['P/L'              ] ,
            'P/VP'          :          row['P/VP'             ] ,
            'PSR'           :          row['PSR'              ] ,
            'DY'            : fix_perc(row['Div.Yield'        ]),
            'P/Ativo'       :          row['P/Ativo'          ] ,
            'P/CapGiro'     :          row['P/Cap.Giro'       ] ,
            'P/EBIT'        :          row['P/EBIT'           ] ,
            'P/AtivCircLiq' :          row['P/Ativ Circ.Liq'  ] ,
            'EV/EBIT'       :          row['EV/EBIT'          ] ,
            'EV/EBITDA'     :          row['EV/EBITDA'        ] ,
            'MrgEbit'       : fix_perc(row['Mrg Ebit'         ]),
            'MrgLiq'        : fix_perc(row['Mrg. Líq.'        ]),
            'LiqCorr'       :          row['Liq. Corr.'       ] ,
            'ROIC'          : fix_perc(row['ROIC'             ]),
            'ROE'           : fix_perc(row['ROE'              ]),
            'Liq2meses'     :          row['Liq.2meses'       ] ,
            'PatLiq'        :          row['Patrim. Líq'      ] ,
            'DivBrut/Pat'   :          row['Dív.Brut/ Patrim.'] ,
            'Cresc5anos'    : fix_perc(row['Cresc. Rec.5a'    ]),
        }

    return results


# Input: string perc pt-br
def fix_perc(val):
    if (val.endswith('%')):
        val = val.replace('.', '' )
        val = val.replace(',', '.')
        val = Decimal(val.rstrip('%')) / 100

    return Decimal(val)


# CSV: ';' separator
def print_csv(data):

    #       Label              hdr    row
    fmt = { 'Papel'        :  ['<6' , '<6'     ] ,
            'Cotacao'      :  ['>9' , '>9,.2f' ] ,
            'P/L'          :  ['>10', '>10,.2f'] ,
            'P/VP'         :  ['>10', '>10,.2f'] ,
            'PSR'          :  ['>8' , '>8,.2f' ] ,
            'DY'           :  ['>7' , '>7,.4f' ] ,
            'P/Ativo'      :  ['>10', '>10,.4f'] ,
            'P/CapGiro'    :  ['>10', '>10,.2f'] ,
            'P/EBIT'       :  ['>9' , '>9,.2f' ] ,
            'P/AtivCircLiq':  ['>13', '>13,.2f'] ,
            'EV/EBIT'      :  ['>10', '>10,.2f'] ,
            'EV/EBITDA'    :  ['>10', '>10,.2f'] ,
            'MrgEbit'      :  ['>9' , '>9,.4f' ] ,
            'MrgLiq'       :  ['>9' , '>9,.4f' ] ,
            'LiqCorr'      :  ['>9' , '>9,.2f' ] ,
            'ROIC'         :  ['>8' , '>8,.4f' ] ,
            'ROE'          :  ['>8' , '>8,.4f' ] ,
            'Liq2meses'    :  ['>16', '>16,.2f'] ,
            'PatLiq'       :  ['>18', '>18,.2f'] ,
            'DivBrut/Pat'  :  ['>12', '>12,.2f'] ,
            'Cresc5anos'   :  ['>10' ,'>10,.4f'] ,
    }

    # print header first
    line = ''
    for label in fmt:
        hdr  = '{:' + fmt[label][0] + '}; '
        line = line + hdr.format( label )
    print(line)


    # print rows
    for key, value in data.items():

        line = ''
        for label in fmt:
            row  = '{:' + fmt[label][1] + '}; '
            line = line + row.format( value[label] )
        print(line)

    return


if __name__ == '__main__':

    data = get_fundamentus()
    print_csv(data)
