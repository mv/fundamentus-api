#!/usr/bin/env python3
#
# Fundamentus v2.0
#   params:
#     - POST parameters
#     - not used anymore: POST is not cacheable
#

def _params( filters={} ):
    """
    Get data from fundamentus:
      URL POST:
        http://fundamentus.com.br/buscaavancada.php
      URL results:
        http://fundamentus.com.br/resultado.php
    """
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
    params.update(filters)

    ##
    ## Busca avançada por empresa
    ##
    url = 'http://www.fundamentus.com.br/resultado.php'
    hdr = {'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',
           'Accept': 'text/html, text/plain, text/css, text/sgml, */*;q=0.01',
           'Accept-Encoding': 'gzip, deflate',
           }

#   content = requests.post(url, headers=hdr, data=params)

    ## parse + load
#   df = pd.read_html(content.text, decimal=",", thousands='.')[0]

    return

