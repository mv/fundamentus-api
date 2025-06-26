
"""
setor:
    Info from .../detalhes.php?setor=
"""

import io
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
    df = pd.read_html(io.StringIO(content.text), decimal=",", thousands='.')[0]

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
## Ref:
##   view-source:https://fundamentus.com.br/buscaavancada.php
##
##   <select name="setor">
##     <option value="" selected></option>
##     <option value="1">Agropecuária</option>
##     ..
##     <option value="43">Viagens e Lazer</option>
##   </select>

_setor = [
   [ 'agro'               , 'Agropecuária'                             ,  1 ] ,
   [ 'saneamento'         , 'Água e Saneamento'                        ,  2 ] ,
   [ 'alimentos'          , 'Alimentos Processados'                    ,  3 ] ,
   [ 'autos'              , 'Automóveis e Motocicletas'                ,  5 ] ,
   [ 'bebidas'            , 'Bebidas'                                  ,  6 ] ,
   [ 'comercio'           , 'Comércio'                                 ,  7 ] ,
   [ 'comercio-distro'    , 'Comércio e Distribuição'                  ,  8 ] ,
   [ 'computadores'       , 'Computadores e Equipamentos'              ,  9 ] ,
   [ 'construcao'         , 'Construção Civil'                         , 10 ] ,
   [ 'engenharia'         , 'Construção e Engenharia'                  , 11 ] ,
   [ 'diversos'           , 'Diversos'                                 , 12 ] ,
   [ 'embalagens'         , 'Embalagens'                               , 13 ] ,
   [ 'energia'            , 'Energia Elétrica'                         , 14 ] ,
   [ 'equipamentos'       , 'Equipamentos'                             , 15 ] ,
   [ 'imoveis'            , 'Exploração de Imóveis'                    , 16 ] ,
   [ 'gas'                , 'Gás'                                      , 17 ] ,
   [ 'holdings'           , 'Holdings Diversificadas'                  , 18 ] ,
   [ 'hoteis-restaurantes', 'Hoteis e Restaurantes'                    , 19 ] ,
   [ 'financeiro'         , 'Intermediários Financeiros'               , 20 ] ,
   [ 'papel'              , 'Madeira e Papel'                          , 21 ] ,
   [ 'maquinas'           , 'Máquinas e Equipamentos'                  , 22 ] ,
   [ 'materiais'          , 'Materiais Diversos'                       , 23 ] ,
   [ 'transporte'         , 'Material de Transporte'                   , 24 ] ,
   [ 'medicamentos'       , 'Medicamentos e Outros Produtos'           , 25 ] ,
   [ 'midia'              , 'Mídia'                                    , 26 ] ,
   [ 'mineracao'          , 'Mineração'                                , 27 ] ,
   [ 'outros'             , 'Outros'                                   , 28 ] ,
   [ 'outros-tit'         , 'Outros Títulos'                           , 29 ] ,
   [ 'petroleo'           , 'Petróleo, Gás e Biocombustíveis'          , 30 ] ,
   [ 'prev-seguros'       , 'Previdência e Seguros'                    , 31 ] ,
   [ 'uso-pessoal'        , 'Produtos de Uso Pessoal e de Limpeza'     , 32 ] ,
   [ 'programas-serv'     , 'Programas e Serviços'                     , 33 ] ,
   [ 'quimicos'           , 'Químicos'                                 , 34 ] ,
   [ 'securitizadoras'    , 'Securitizadoras de Recebíveis'            , 35 ] ,
   [ 'saude'              , 'Serv.Méd.Hospit. Análises e Diagnósticos' ,  4 ] ,
   [ 'servicos-diversos'  , 'Serviços Diversos'                        , 36 ] ,
   [ 'fin-diversos'       , 'Serviços Financeiros Diversos'            , 37 ] ,
   [ 'siderurgia'         , 'Siderurgia e Metalurgia'                  , 38 ] ,
   [ 'tecidos'            , 'Tecidos, Vestuário e Calçados'            , 39 ] ,
   [ 'telecom'            , 'Telecomunicações'                         , 40 ] ,
   [ 'transporte'         , 'Transporte'                               , 41 ] ,
   [ 'utilidades'         , 'Utilidades Domésticas'                    , 42 ] ,
   [ 'viagens'            , 'Viagens e Lazer'                          , 43 ] ,
]
##

# setup/load
df = _init_setor()


