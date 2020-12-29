
from fundamentus import detalhes

import pandas as pd


def test_get_detalhes_raw():

    # html_tables
    ht = detalhes.get_detalhes_raw('WEGE3')
    assert len(ht) == 5

def test_get_detalhes_raw_df0():
    ht = detalhes.get_detalhes_raw('WEGE3')
    df = ht[0]
    assert len(df)         == 5
    assert len(df.columns) == 4
    assert df.iloc[0][1]   == 'WEGE3'


def test_get_detalhes_raw_df1():
    ht = detalhes.get_detalhes_raw('WEGE3')
    df = ht[1]
    assert len(df)         == 2
    assert len(df.columns) == 4
    assert df.iloc[0][0]   == '?Valor de mercado'
    assert df.iloc[1][0]   == '?Valor da firma'


def test_get_detalhes_raw_df2():
    ht = detalhes.get_detalhes_raw('WEGE3')
    df = ht[2]
    assert len(df)         > 5
    assert len(df.columns) == 6
    assert df.iloc[1][2]   == '?P/L'
    assert df.iloc[1][4]   == '?LPA'


def test_get_detalhes_raw_df3():
    ht = detalhes.get_detalhes_raw('WEGE3')
    df = ht[3]
    assert len(df)         == 4
    assert len(df.columns) == 4
    assert df.iloc[1][0]   == '?Ativo'
    assert df.iloc[3][2]   == '?Patrim. Líq'


def test_get_detalhes_raw_df4():
    ht = detalhes.get_detalhes_raw('WEGE3')
    df = ht[4]
    assert len(df)         == 5
    assert len(df.columns) == 4
    assert df.iloc[3][0]   == '?EBIT'
    assert df.iloc[3][2]   == '?EBIT'


def test_get_detalhes_papel():

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

    df = detalhes.get_detalhes_papel('WEGE3')

    assert len(df) > 0
    assert list(df.columns) == cols
    assert df['Papel'][0]   == 'WEGE3'


def test_get_detalhes_list():
    df = detalhes.get_detalhes_list(['ITSA4','WEGE3'])
    assert len(df) == 2
    assert df.index[0]   == 'ITSA4'
    assert df.index[1]   == 'WEGE3'


def test_get_detalhes__as_list():
    df = detalhes.get_detalhes(['ITSA4','WEGE3'])
    assert len(df) == 2
    assert df.index[0]   == 'ITSA4'
    assert df.index[1]   == 'WEGE3'


def test_get_detalhes__as_papel_1():
    df = detalhes.get_detalhes('ITSA4')
    assert df['Papel'][0] == 'ITSA4'

def test_get_detalhes__as_papel_2():
    df = detalhes.get_detalhes('WEGE3')
    assert df['Papel'][0] == 'WEGE3'


