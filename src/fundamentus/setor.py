
"""
setor:
    Info from .../detalhes.php?setor=
"""

import requests
import requests_cache
import pandas   as pd
import time, logging

from   tabulate import tabulate


def list_papel_setor(setor=None):
    """
    Setor: ...

    Output:
      List
    """

    ## GET: setor
    url = 'http://www.fundamentus.com.br/resultado.php?setor={}'.format(setor)

    hdr = {'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201' ,
           'Accept': 'text/html, text/plain, text/css, text/sgml, */*;q=0.01' ,
           'Accept-Encoding': 'gzip, deflate' ,
           }

    with requests_cache.enabled():
        content = requests.get(url, headers=hdr)

        if content.from_cache:
            logging.debug('.../resultado.php?setor={}: [CACHED]'.format(setor))
        else: # pragma: no cover
            logging.debug('.../resultado.php?setor={}: sleeping...'.format(setor))
            time.sleep(.500) # 500 ms


    ## parse + load
    df = pd.read_html(content.text, decimal=",", thousands='.')[0]

    ##
    return list(df['Papel'])


def get_setor_id(label):
    return df.T[label]['id']

def print_setores():
    print( tabulate(df, headers=['label','desc','id'], tablefmt='presto') )
    return


def _init_setor():
    data = pd.DataFrame(_setor, columns=['label','desc','id'])
    data.index = data['label']

    return data[['desc','id']]


## Setores:
_setor = [
   [ 'agro'            , 'Agropecuária'                       , 42 ] ,
   [ 'saneamento'      , 'Água e Saneamento'                  , 33 ] ,
   [ 'alimentos'       , 'Alimentos'                          , 15 ] ,
   [ 'bebidas'         , 'Bebidas'                            , 16 ] ,
   [ 'com1'            , 'Comércio'                           , 27 ] ,
   [ 'com2'            , 'Comércio'                           , 12 ] ,
   [ 'com3'            , 'Comércio e Distribuição'            , 20 ] ,
   [ 'computadores'    , 'Computadores e Equipamentos'        , 28 ] ,
   [ 'construcao'      , 'Construção e Engenharia'            , 13 ] ,
   [ 'engenharia'      , 'Construção e Engenharia'            , 13 ] ,
   [ 'diversos'        , 'Diversos'                           , 26 ] ,
   [ 'embalagens'      , 'Embalagens'                         , 6  ] ,
   [ 'energia'         , 'Energia Elétrica'                   , 32 ] ,
   [ 'equipamentos'    , 'Equipamentos Elétricos'             , 9  ] ,
   [ 'imoveis'         , 'Exploração de Imóveis'              , 39 ] ,
   [ 'financeiro'      , 'Financeiros'                        , 35 ] ,
   [ 'fumo'            , 'Fumo'                               , 17 ] ,
   [ 'gas'             , 'Gás'                                , 34 ] ,
   [ 'holdings'        , 'Holdings Diversificadas'            , 40 ] ,
   [ 'hoteis'          , 'Hoteis e Restaurantes'              , 24 ] ,
   [ 'restaurantes'    , 'Hoteis e Restaurantes'              , 24 ] ,
   [ 'papel'           , 'Madeira e Papel'                    , 5  ] ,
   [ 'maquinas'        , 'Máquinas e Equipamentos'            , 10 ] ,
   [ 'materiais'       , 'Materiais Diversos'                 , 7  ] ,
   [ 'transporte'      , 'Material de Transporte'             , 8  ] ,
   [ 'midia'           , 'Mídia'                              , 23 ] ,
   [ 'mineracao'       , 'Mineração'                          , 2  ] ,
   [ 'outros'          , 'Outros'                             , 41 ] ,
   [ 'petroleo'        , 'Petróleo, Gás e Biocombustíveis'    , 1  ] ,
   [ 'previdencia'     , 'Previdência e Seguros'              , 38 ] ,
   [ 'seguros'         , 'Previdência e Seguros'              , 38 ] ,
   [ 'usopessoal'      , 'Prods. de Uso Pessoal e de Limpeza' , 18 ] ,
   [ 'limpeza'         , 'Prods. de Uso Pessoal e de Limpeza' , 18 ] ,
   [ 'programas'       , 'Programas e Serviços'               , 29 ] ,
   [ 'quimicos'        , 'Químicos'                           , 4  ] ,
   [ 'saude'           , 'Saúde'                              , 19 ] ,
   [ 'securitizadoras' , 'Securitizadoras de Recebíveis'      , 36 ] ,
   [ 'servicos'        , 'Serviços'                           , 11 ] ,
   [ 'finandiversos'   , 'Serviços Financeiros Diversos'      , 37 ] ,
   [ 'siderurgia'      , 'Siderurgia e Metalurgia'            , 3  ] ,
   [ 'tecidos'         , 'Tecidos, Vestuário e Calçados'      , 21 ] ,
   [ 'vestuario'       , 'Tecidos, Vestuário e Calçados'      , 21 ] ,
   [ 'telecom'         , 'Telecomunicações'                   , 43 ] ,
   [ 'telefoniafixa'   , 'Telefonia Fixa'                     , 30 ] ,
   [ 'telefoniamovel'  , 'Telefonia Móvel'                    , 31 ] ,
   [ 'transporte'      , 'Transporte'                         , 14 ] ,
   [ 'utilidades'      , 'Utilidades Domésticas'              , 22 ] ,
   [ 'viagens'         , 'Viagens e Lazer'                    , 25 ] ,
]
##

# setup/load
df = _init_setor()


