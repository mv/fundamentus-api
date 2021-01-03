
from fundamentus import detalhes

import pytest
import pandas as pd


###
lst_papel = ['ABEV3','ITSA4','WEGE3']

@pytest.fixture(params=lst_papel)
def each_papel(request):
    return request.param


def test_get_detalhes_raw_len(each_papel):
    # GIVEN a 'raw' 'detalhes' page
    # WHEN  papel is 'WEGE3'
    # THEN  pd.read_html() must return 5 html tables
    ht = detalhes.get_detalhes_raw(each_papel)
    assert len(ht) == 5

def test_get_detalhes_raw_df0(each_papel):
    # GIVEN a 'raw' 'detalhes' page
    # WHEN  papel is 'WEGE3'
    # THEN  first df must be 4x5
    ht = detalhes.get_detalhes_raw(each_papel)
    df = ht[0]
    assert len(df)         == 5
    assert len(df.columns) == 4
    assert df.iloc[0][1]   == each_papel


def test_get_detalhes_raw_df1(each_papel):
    # GIVEN a 'raw' 'detalhes' page
    # WHEN  papel is 'WEGE3'
    # THEN  second df must be 4x2
    ht = detalhes.get_detalhes_raw(each_papel)
    df = ht[1]
    assert len(df)         == 2
    assert len(df.columns) == 4
    assert df.iloc[0][0]   == '?Valor de mercado'
    assert df.iloc[1][0]   == '?Valor da firma'


def test_get_detalhes_raw_df2(each_papel):
    # GIVEN a 'raw' 'detalhes' page
    # WHEN  papel is 'WEGE3'
    # THEN  third df must be 6x5
    ht = detalhes.get_detalhes_raw(each_papel)
    df = ht[2]
    assert len(df)         == 12
    assert len(df.columns) == 6
    assert df.iloc[1][2]   == '?P/L'
    assert df.iloc[1][4]   == '?LPA'


def test_get_detalhes_raw_df3(each_papel):
    # GIVEN a 'raw' 'detalhes' page
    # WHEN  papel is 'WEGE3'
    # THEN  forth df must be 4x4
    ht = detalhes.get_detalhes_raw(each_papel)
    df = ht[3]
    assert len(df)         == 4
    assert len(df.columns) == 4
    assert df.iloc[1][0]   == '?Ativo'
    assert df.iloc[3][2]   == '?Patrim. Líq'


def test_get_detalhes_raw_df4(each_papel):
    # GIVEN a 'raw' 'detalhes' page
    # WHEN  papel is 'WEGE3'
    # THEN  last df must be 4x5
    ht = detalhes.get_detalhes_raw(each_papel)
    df = ht[4]
    assert len(df)         == 5
    assert len(df.columns) == 4
    assert df.iloc[3][0]   == '?EBIT'
    assert df.iloc[3][2]   == '?EBIT'


def test_get_detalhes_papel(each_papel):
    # GIVEN a final 'detalhes' dataframe
    # WHEN  papel is 'WEGE3'
    # THEN  columns must be the following

    cols = ['Papel', 'Tipo', 'Empresa', 'Setor', 'Subsetor', 'Cotacao',
       'Data_ult_cot', 'Min_52_sem', 'Max_52_sem', 'Vol_med_2m',
       'Valor_de_mercado', 'Valor_da_firma', 'Ult_balanco_processado',
       'Nro_Acoes', 'PL', 'PVP', 'PEBIT', 'PSR', 'PAtivos', 'PCap_Giro',
       'PAtiv_Circ_Liq', 'Div_Yield', 'EV_EBITDA', 'EV_EBIT', 'Cres_Rec_5a',
       'LPA', 'VPA', 'Marg_Bruta', 'Marg_EBIT', 'Marg_Liquida', 'EBIT_Ativo',
       'ROIC', 'ROE', 'Liquidez_Corr', 'Div_Br_Patrim', 'Giro_Ativos', 'Ativo',
       'Disponibilidades', 'Ativo_Circulante', 'Div_Bruta', 'Div_Liquida',
       'Patrim_Liq', 'Receita_Liquida_12m', 'EBIT_12m', 'Lucro_Liquido_12m',
       'Receita_Liquida_3m', 'EBIT_3m', 'Lucro_Liquido_3m']

    df = detalhes.get_detalhes_papel(each_papel)

    assert len(df) > 0
    assert list(df.columns) == cols
    assert df['Papel'][0]   == each_papel


###
def test_get_detalhes_list():
    # GIVEN calling 'detalhes_list()' explicitly
    # WHEN  list is 'ITSA4' and 'WEGE3'
    # THEN  list must contain 2 x 'papel' in sorted order
    df = detalhes.get_detalhes_list(['ITSA4','WEGE3'])
    assert len(df) == 2
    assert df.index[0]   == 'ITSA4'
    assert df.index[1]   == 'WEGE3'


def test_get_papel__as_list():
    # GIVEN calling 'get_papel()' with a list
    # WHEN  list is 'ITSA4' and 'WEGE3'
    # THEN  list must contain 2 x 'papel' in sorted order
    df = detalhes.get_papel(['ITSA4','WEGE3'])
    assert len(df) == 2
    assert df.index[0]   == 'ITSA4'
    assert df.index[1]   == 'WEGE3'


###
def test_get_papel__as_papel(each_papel):
    df = detalhes.get_papel(each_papel)
    assert df['Papel'][0] == each_papel


###
def test_list_papel_all__len():
    # GIVEN calling 'list_papel_all()'
    # THEN  list must contain more than 5 elements
    lst = detalhes.list_papel_all()
    assert len(lst) > 5


###
def test_list_papel_all__in(each_papel):
    # GIVEN calling 'list_papel_all()'
    # THEN  list must contain at least
    #       'ABEV3','ITSA4','WEGE3'
    lst = detalhes.list_papel_all()
    assert each_papel in lst


