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
    ##
    params = {'pl_min'          : '',
              'pl_max'          : '',
              'pvp_min'         : '',
              'pvp_max'         : '',
              'psr_min'         : '',
              'psr_max'         : '',
              'divy_min'        : '',
              'divy_max'        : '',
              'pativos_min'     : '',
              'pativos_max'     : '',
              'pcapgiro_min'    : '',
              'pcapgiro_max'    : '',
              'pebit_min'       : '',
              'pebit_max'       : '',
              'fgrah_min'       : '',
              'fgrah_max'       : '',
              'firma_ebit_min'  : '',
              'firma_ebit_max'  : '',
              'firma_ebitda_min': '',
              'firma_ebitda_max': '',
              'margemebit_min'  : '',
              'margemebit_max'  : '',
              'margemliq_min'   : '',
              'margemliq_max'   : '',
              'liqcorr_min'     : '',
              'liqcorr_max'     : '',
              'roic_min'        : '',
              'roic_max'        : '',
              'roe_min'         : '',
              'roe_max'         : '',
              'liq_min'         : '',
              'liq_max'         : '',
              'patrim_min'      : '',
              'patrim_max'      : '',
              'divbruta_min'    : '',
              'divbruta_max'    : '',
              'tx_cresc_rec_min': '',
              'tx_cresc_rec_max': '',
              'setor'           : '',
              'negociada'       : 'ON',
              'ordem'           : '1',
              'x'               : '28',
              'y'               : '16'}

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

    content = requests.get(url, headers=hdr).text

    # parse
    df = pd.read_html(content, decimal=",", thousands='.')[0]

    # load
    results = OrderedDict()

    for row in df.to_dict('records'):
        results[row['Papel']] = {
            # fix header names
            'Cotacao'       :          row['Cotação'          ] ,
            'P/L'           :          row['P/L'              ] ,
            'P/VP'          :          row['P/VP'             ] ,
            'PSR'           :          row['PSR'              ] ,
            'DY'            : fix_perc(row['Div.Yield'        ]),
            'P/Ativo'       :          row['P/Ativo'          ] ,
            'P/Cap.Giro'    :          row['P/Cap.Giro'       ] ,
            'P/EBIT'        :          row['P/EBIT'           ] ,
            'P/ACL'         :          row['P/Ativ Circ.Liq'  ] ,
            'EV/EBIT'       :          row['EV/EBIT'          ] ,
            'EV/EBITDA'     :          row['EV/EBITDA'        ] ,
            'Mrg.Ebit'      : fix_perc(row['Mrg Ebit'         ]),
            'Mrg.Liq.'      : fix_perc(row['Mrg. Líq.'        ]),
            'Liq.Corr.'     :          row['Liq. Corr.'       ] ,
            'ROIC'          : fix_perc(row['ROIC'             ]),
            'ROE'           : fix_perc(row['ROE'              ]),
            'Liq.2meses'    :          row['Liq.2meses'       ] ,
            'Pat.Liq'       :          row['Patrim. Líq'      ] ,
            'Div.Brut/Pat.' :          row['Dív.Brut/ Patrim.'] ,
            'Cresc.5anos'   : fix_perc(row['Cresc. Rec.5a'    ]),
        }

    return results


# Input: string perc pt-br
def fix_perc(val):
    if (val.endswith('%')):
        val = val.replace('.', '' )
        val = val.replace(',', '.')
        val = Decimal(val.rstrip('%')) / 100

    return val


# CSV: ';' separator
def print_csv(data):

     #         Papel   Cotacao  P/L     P/VP     PSR     DY      P/Ativo P/CapGir P/EBIT   P/ACL  EV/EBIT  EV/EBITDA Mrg.Ebit Mrg.Liq. Liq.Corr. ROIC     ROE       Liq.2meses Pat.Liq Div.Brut/Pat. Cresc.5anos))
    fmt_hdr = '{0:<6}; {1:<7}; {2:<10}; {3:<7}; {4:<8}; {5:<7}; {6:<10}; {7:<10}; {8:<8}; {9:<8}; {10:<8}; {11:<10}; {12:<8}; {13:<8}; {14:<9}; {15:<8}; {16:<8}; {17:<15};'
    fmt_row = '{0:<6}; {1:>7}; {2:>10}; {3:>7}; {4:>8}; {5:>7}; {6:>10}; {7:>10}; {8:>8}; {9:>8}; {10:>8}; {11:>10}; {12:>8}; {13:>8}; {14:>9}; {15:>8}; {16:>8}; {17:>15};'

    print(fmt_hdr.format('Papel',
                         'Cotacao',
                         'P/L',
                         'P/VP',
                         'PSR',
                         'DY',
                         'P/Ativo',
                         'P/Cap.Giro',
                         'P/EBIT',
                         'P/ACL',
                         'EV/EBIT',
                         'EV/EBITDA',
                         'Mrg.Ebit',
                         'Mrg.Liq.',
                         'Liq.Corr.',
                         'ROIC',
                         'ROE',
                         'Liq.2meses',
                         'Pat.Liq',
                         'Div.Brut/Pat.',
                         'Cresc.5anos',
                         ))

    for key, value in data.items():
        print(fmt_row.format(key,
                             value['Cotacao'],
                             value['P/L'],
                             value['P/VP'],
                             value['PSR'],
                             value['DY'],
                             value['P/Ativo'],
                             value['P/Cap.Giro'],
                             value['P/EBIT'],
                             value['P/ACL'],
                             value['EV/EBIT'],
                             value['EV/EBITDA'],
                             value['Mrg.Ebit'],
                             value['Mrg.Liq.'],
                             value['Liq.Corr.'],
                             value['ROIC'],
                             value['ROE'],
                             value['Liq.2meses'],
                             value['Pat.Liq'],
                             value['Div.Brut/Pat.'],
                             value['Cresc.5anos'],
                             ))



if __name__ == '__main__':

    data = get_fundamentus()
    print_csv(data)

