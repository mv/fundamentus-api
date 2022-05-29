
from fundamentus import fii

import pytest
import pandas as pd


###
lst_fiis = ['HGLG11','BCFF11']

@pytest.fixture(params=lst_fiis)
def each_papel(request):
    return request.param


def test_get_fii_raw_len(each_papel):
    # GIVEN a 'raw' 'detalhes' page
    # WHEN  papel is 'HGLG11'
    # THEN  pd.read_html() must return 6 html tables
    ht = fii.get_detalhes_fii_raw(each_papel)
    assert len(ht) == 6

def test_get_detalhes_fii_raw_df0(each_papel):
    # GIVEN a 'raw' 'detalhes' page
    # WHEN  papel is 'HGLG11'
    # THEN  first df must be 4x6
    ht = fii.get_detalhes_fii_raw(each_papel)
    df = ht[0]
    assert len(df)         == 5
    assert len(df.columns) == 4
    assert df.iloc[0][1]   == each_papel


def test_get_detalhes_fii_raw_df1(each_papel):
    # GIVEN a 'raw' 'detalhes' page
    # WHEN  papel is 'HGLG11'
    # THEN  second df must be 4x2
    ht = fii.get_detalhes_fii_raw(each_papel)
    df = ht[1]
    assert len(df)         == 2
    assert len(df.columns) == 4
    assert df.iloc[0][0]   == '?Valor de mercado'
    assert df.iloc[1][0]   == '?Relatório'


def test_get_detalhes_fii_raw_df2(each_papel):
    # GIVEN a 'raw' 'detalhes' page
    # WHEN  papel is 'HGLG11'
    # THEN  third df must be 6x5
    ht = fii.get_detalhes_fii_raw(each_papel)
    df = ht[2]
    assert len(df)         == 12
    assert len(df.columns) == 6
    assert df.iloc[1][2]   == '?FFO Yield'
    assert df.iloc[1][4]   == '?FFO/Cota'


def test_get_detalhes_raw_df3(each_papel):
    # GIVEN a 'raw' 'detalhes' page
    # WHEN  papel is 'HGLG11'
    # THEN  forth df must be 4x4
    ht = fii.get_detalhes_fii_raw(each_papel)
    df = ht[3]
    assert len(df)         == 2
    assert len(df.columns) == 6


def test_get_detalhes_raw_df4(each_papel):
    # GIVEN a 'raw' 'detalhes' page
    # WHEN  papel is 'HGLG11'
    # THEN  last df must be 4x5
    ht = fii.get_detalhes_fii_raw(each_papel)
    df = ht[4]
    assert len(df)         == 4
    assert len(df.columns) == 6
    assert df.iloc[3][0]   == '?Imóveis/PL do FII'
    assert df.iloc[3][2]   == '?Preço do m2'


def test_get_detalhes_papel(each_papel):
    # GIVEN a final 'detalhes' dataframe
    # WHEN  papel is 'HGLG11'
    # THEN  columns must be the following

    cols = ['FII', 'Nome',  'Mandato',  'Segmento',  'Gestao',
    'Cotacao',  'Data_ult_cot',  'Min_52_sem',  'Max_52_sem',
    'Vol_med_2m',  'Valor_de_mercado',  'Relatorio',  'Nro_Cotas',
    'Ult_Info_Trimestral',  'FFO_Yield',  'Div_Yield',  'PVP',
    'Resultado',  'Ultimos_12_meses',  'Receita',  'Venda_de_ativos', 
    'FFO',  'Rend_Distribuido',  'Balanco_Patrimonial',  'Ativos',  
    'FFOCota',  'Dividendocota',  'VPCota',  'Ultimos_3_meses',  'Patrim_Liquido',  
    'Qtd_Unidades_12m',  'ImoveisPL_do_FII_12m',  'Aluguelm2_3m',  
    'Preco_do_m2_3m']

    df = fii.get_detalhes_fii(each_papel)

    assert len(df) > 0
    assert list(df.columns) == cols
    assert df['FII'][0]   == each_papel


###
def test_get_detalhes_fii_list():
    # GIVEN calling 'detalhes_list()' explicitly
    # WHEN  list is 'BCFF11' and 'HGLG11'
    # THEN  list must contain 2 x 'papel' in sorted order
    df = fii.get_detalhes_fii_list(['BCFF11','HGLG11'])
    assert len(df) == 2
    assert df.index[0]   == 'BCFF11'
    assert df.index[1]   == 'HGLG11'


def test_get_fii_as_list():
    # GIVEN calling 'get_papel()' with a list
    # WHEN  list is 'BCFF11' and 'HGLG11'
    # THEN  list must contain 2 x 'papel' in sorted order
    df = fii.get_fii(['BCFF11','HGLG11'])
    assert len(df) == 2
    assert df.index[0]   == 'BCFF11'
    assert df.index[1]   == 'HGLG11'


###
def test_get_fii_as_papel(each_papel):
    df = fii.get_fii(each_papel)
    assert df['FII'][0] == each_papel

