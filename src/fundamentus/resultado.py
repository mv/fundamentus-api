"""
resultado:
    Info from http://fundamentus.com.br/resultado.php
"""


import fundamentus.utils as utils

import requests
import requests_cache
import pandas   as pd
import time, logging

from tabulate import tabulate


def get_resultado_raw():
    """
    Get data from fundamentus:
      URL:
        http://fundamentus.com.br/resultado.php

    RAW:
      DataFrame preserves original HTML header names

    Output:
      DataFrame
    """

    ##
    ## Busca avançada por empresa
    ##
    url = 'http://www.fundamentus.com.br/resultado.php'
    hdr = {'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',
           'Accept': 'text/html, text/plain, text/css, text/sgml, */*;q=0.01',
           'Accept-Encoding': 'gzip, deflate',
           }

    with requests_cache.enabled():
        content = requests.get(url, headers=hdr)

        if content.from_cache:
            logging.debug('.../resultado.php: [CACHED]')
        else: # pragma: no cover
            logging.debug('.../resultado.php: sleeping...')
            time.sleep(.500) # 500 ms


    ## parse + load
    df = pd.read_html(content.text, decimal=",", thousands='.')[0]

    ## Fix: percent string
    df['Div.Yield']     = utils.perc_to_float( df['Div.Yield']     )
    df['Mrg Ebit']      = utils.perc_to_float( df['Mrg Ebit']      )
    df['Mrg. Líq.']     = utils.perc_to_float( df['Mrg. Líq.']     )
    df['ROIC']          = utils.perc_to_float( df['ROIC']          )
    df['ROE']           = utils.perc_to_float( df['ROE']           )
    df['Cresc. Rec.5a'] = utils.perc_to_float( df['Cresc. Rec.5a'] )

    ## index by 'Papel', instead of 'int'
    df.index = df['Papel']
    df.drop('Papel', axis='columns', inplace=True)
    df.sort_index(inplace=True)

    ## naming
    df.name = 'Fundamentus: HTML names'
    df.columns.name = 'Multiples'
    df.index.name = 'papel'

    ## return sorted by 'papel'
    return df


def get_resultado():
    """
    Data from fundamentus, fixing header names.
      URL:
        http://fundamentus.com.br/resultado.php
      Obs:
        DataFrame uses short header names
    Output:
      DataFrame
    """

    ## get RAW data
    data1 = get_resultado_raw()

    ## rename!
    data2 = _rename_cols(data1)

    ## metadata
    data2.name = 'Fundamentus: short names'
    data2.columns.name = 'Multiples'
    data2.index.name = 'papel'

    ## remove duplicates
#   df = data2.drop_duplicates(subset=['cotacao','pl','pvp'], keep='last')
    df = data2.drop_duplicates(keep='first')

    return df


def _rename_cols(data):
    """
    Rename columns in DataFrame
      - use a valid Python identifier
      - so each column can be a DataFrame property
      - Example:
          df.pl > 0
    """

    df2 = pd.DataFrame()

    ## Fix: rename columns
    df2['cotacao'  ] = data['Cotação'          ]
    df2['pl'       ] = data['P/L'              ]
    df2['pvp'      ] = data['P/VP'             ]
    df2['psr'      ] = data['PSR'              ]
    df2['dy'       ] = data['Div.Yield'        ]
    df2['pa'       ] = data['P/Ativo'          ]
    df2['pcg'      ] = data['P/Cap.Giro'       ]
    df2['pebit'    ] = data['P/EBIT'           ]
    df2['pacl'     ] = data['P/Ativ Circ.Liq'  ]
    df2['evebit'   ] = data['EV/EBIT'          ]
    df2['evebitda' ] = data['EV/EBITDA'        ]
    df2['mrgebit'  ] = data['Mrg Ebit'         ]
    df2['mrgliq'   ] = data['Mrg. Líq.'        ]
    df2['roic'     ] = data['ROIC'             ]
    df2['roe'      ] = data['ROE'              ]
    df2['liqc'     ] = data['Liq. Corr.'       ]
    df2['liq2m'    ] = data['Liq.2meses'       ]
    df2['patrliq'  ] = data['Patrim. Líq'      ]
    df2['divbpatr' ] = data['Dív.Brut/ Patrim.']
    df2['c5y'      ] = data['Cresc. Rec.5a'    ]

    return df2

