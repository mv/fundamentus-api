#!/usr/bin/env python3

import re
import urllib.request
import urllib.parse
import http.cookiejar

from lxml.html   import fragment_fromstring
from collections import OrderedDict
from decimal     import Decimal


def get_fundamentus(filters={}, *args, **kwargs):

    # Parametros usados em 'Busca avancada por empresa'
    # Parametros em branco retornam todas as empresas disponiveis
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

    params.update(filters)


    # Busca avançada por empresa
    url = 'http://www.fundamentus.com.br/resultado.php'

    cookie_jar = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201'),
                         ('Accept', 'text/html, text/plain, text/css, text/sgml, */*;q=0.01')]

    with opener.open(url, urllib.parse.urlencode(params).encode('UTF-8')) as link:
        content = link.read().decode('ISO-8859-1')

    pattern = re.compile('<table id="resultado".*</table>', re.DOTALL)
    re_data = re.findall(pattern, content)[0]
    page    = fragment_fromstring(re_data)

    results = OrderedDict()

    for rows in page.xpath('tbody')[0].findall("tr"):

        results.update(
            {rows.getchildren()[0][0].getchildren()[0].text:
                { 'Cotacao'       : to_decimal(rows.getchildren()[1].text),
                  'P/L'           : to_decimal(rows.getchildren()[2].text),
                  'P/VP'          : to_decimal(rows.getchildren()[3].text),
                  'PSR'           : to_decimal(rows.getchildren()[4].text),
                  'DY'            : to_decimal(rows.getchildren()[5].text),
                  'P/Ativo'       : to_decimal(rows.getchildren()[6].text),
                  'P/Cap.Giro'    : to_decimal(rows.getchildren()[7].text),
                  'P/EBIT'        : to_decimal(rows.getchildren()[8].text),
                  'P/ACL'         : to_decimal(rows.getchildren()[9].text),
                  'EV/EBIT'       : to_decimal(rows.getchildren()[10].text),
                  'EV/EBITDA'     : to_decimal(rows.getchildren()[11].text),
                  'Mrg.Ebit'      : to_decimal(rows.getchildren()[12].text),
                  'Mrg.Liq.'      : to_decimal(rows.getchildren()[13].text),
                  'Liq.Corr.'     : to_decimal(rows.getchildren()[14].text),
                  'ROIC'          : to_decimal(rows.getchildren()[15].text),
                  'ROE'           : to_decimal(rows.getchildren()[16].text),
                  'Liq.2meses'    : to_decimal(rows.getchildren()[17].text),
                  'Pat.Liq'       : to_decimal(rows.getchildren()[18].text),
                  'Div.Brut/Pat.' : to_decimal(rows.getchildren()[19].text),
                  'Cresc.5anos'   : to_decimal(rows.getchildren()[20].text)
                }
            }
        )
        #
        # results.items()
        #   ([('XXX3': {'Cotacao': Decimal('10.10'),
        #               'P/L':     Decimal('09.90'),
        #               ...
        #              }),
        #     ('YYY4': {'Cotacao': Decimal('12.12'),
        #               'P/L':     Decimal('08.80'),
        #               ...
        #              }),
        #   ])
        #
        # results.keys()
        #   (['XXX3', 'YYY4'])
        #
        # results['XXX3']
        #   {'Cotacao': Decimal('10.10'), 'P/L': Decimal('09.90'),...}
        #
        # results['XXX3']['P/L']
        #   Decimal('09.90')
        #

    return results


# Input: string formato pt-br
# Output: python Decimal
def to_decimal(string):
    string = string.replace('.', '' )
    string = string.replace(',', '.')

    if (string.endswith('%')):
        return Decimal(string[:-1]) / 100
    else:
        return Decimal(string)


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

