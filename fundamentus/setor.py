#!/usr/bin/env python3
#
#

import requests
import requests_cache
import pandas   as pd


def get_setor_data(setor=None):
    """
    """

    ##
    ## Busca avançada por empresa
    ##
    url = 'http://www.fundamentus.com.br/resultado.php?setor={}'.format(setor)

    hdr = {'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201' ,
           'Accept': 'text/html, text/plain, text/css, text/sgml, */*;q=0.01' ,
           'Accept-Encoding': 'gzip, deflate' ,
           }

    with requests_cache.enabled():
        content = requests.get(url, headers=hdr)

    ## parse + load
    df = pd.read_html(content.text, decimal=",", thousands='.')[0]

    ##
    return list(df['Papel'])


def list_setor():
    ## Setores:
    setor = [
       [ 'agro'            , 42 , 'Agropecuária'                            ] ,
       [ 'saneamento'      , 33 , 'Água e Saneamento'                       ] ,
       [ 'alimentos'       , 15 , 'Alimentos'                               ] ,
       [ 'bebidas'         , 16 , 'Bebidas'                                 ] ,
       [ 'com1'            , 27 , 'Comércio'                                ] ,
       [ 'com2'            , 12 , 'Comércio'                                ] ,
       [ 'com3'            , 20 , 'Comércio e Distribuição'                 ] ,
       [ 'computadores'    , 28 , 'Computadores e Equipamentos'             ] ,
       [ 'construcao'      , 13 , 'Construção e Engenharia'                 ] ,
       [ 'engenharia'      , 13 , 'Construção e Engenharia'                 ] ,
       [ 'diversos'        , 26 , 'Diversos'                                ] ,
       [ 'embalagens'      , 6  , 'Embalagens'                              ] ,
       [ 'energia'         , 32 , 'Energia Elétrica'                        ] ,
       [ 'equipamentos'    , 9  , 'Equipamentos Elétricos'                  ] ,
       [ 'imoveis'         , 39 , 'Exploração de Imóveis'                   ] ,
       [ 'financeiro'      , 35 , 'Financeiros'                             ] ,
       [ 'fumo'            , 17 , 'Fumo'                                    ] ,
       [ 'gas'             , 34 , 'Gás'                                     ] ,
       [ 'holdings'        , 40 , 'Holdings Diversificadas'                 ] ,
       [ 'hoteis'          , 24 , 'Hoteis e Restaurantes'                   ] ,
       [ 'restaurantes'    , 24 , 'Hoteis e Restaurantes'                   ] ,
       [ 'papel'           , 5  , 'Madeira e Papel'                         ] ,
       [ 'maquinas'        , 10 , 'Máquinas e Equipamentos'                 ] ,
       [ 'materiais'       , 7  , 'Materiais Diversos'                      ] ,
       [ 'transporte'      , 8  , 'Material de Transporte'                  ] ,
       [ 'midia'           , 23 , 'Mídia'                                   ] ,
       [ 'mineracao'       , 2  , 'Mineração'                               ] ,
       [ 'outros'          , 41 , 'Outros'                                  ] ,
       [ 'petroleo'        , 1  , 'Petróleo, Gás e Biocombustíveis'         ] ,
       [ 'previdencia'     , 38 , 'Previdência e Seguros'                   ] ,
       [ 'seguros'         , 38 , 'Previdência e Seguros'                   ] ,
       [ 'usopessoal'      , 18 , 'Prods. de Uso Pessoal e de Limpeza'      ] ,
       [ 'limpeza'         , 18 , 'Prods. de Uso Pessoal e de Limpeza'      ] ,
       [ 'programas'       , 29 , 'Programas e Serviços'                    ] ,
       [ 'quimicos'        , 4  , 'Químicos'                                ] ,
       [ 'saude'           , 19 , 'Saúde'                                   ] ,
       [ 'securitizadoras' , 36 , 'Securitizadoras de Recebíveis'           ] ,
       [ 'servicos'        , 11 , 'Serviços'                                ] ,
       [ 'finandiversos'   , 37 , 'Serviços Financeiros Diversos'           ] ,
       [ 'siderurgia'      , 3  , 'Siderurgia e Metalurgia'                 ] ,
       [ 'tecidos'         , 21 , 'Tecidos, Vestuário e Calçados'           ] ,
       [ 'vestuario'       , 21 , 'Tecidos, Vestuário e Calçados'           ] ,
       [ 'telecom'         , 43 , 'Telecomunicações'                        ] ,
       [ 'telefoniafixa'   , 30 , 'Telefonia Fixa'                          ] ,
       [ 'telefoniamovel'  , 31 , 'Telefonia Móvel'                         ] ,
       [ 'transporte'      , 14 , 'Transporte'                              ] ,
       [ 'utilidades'      , 22 , 'Utilidades Domésticas'                   ] ,
       [ 'viagens'         , 25 , 'Viagens e Lazer'                         ] ,
    ]
    ##

    return setor


def get_setor_id():
    pass;

