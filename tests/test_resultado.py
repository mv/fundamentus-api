
from fundamentus import resultado

import pytest
import pandas as pd


@pytest.fixture(name='df_resultado_raw', scope='session')
def _get_resultado_raw():
    df = resultado.get_resultado_raw()
    return df


###
def test_get_resultado_raw_len(df_resultado_raw):
    # GIVEN a 'resultado_raw' df
    # THEN  it must have '> 0' rows
    assert len(df_resultado_raw) > 0


###
def test_get_resultado_raw_index_name(df_resultado_raw):
    # GIVEN a 'resultado_raw' df
    # THEN  it must have 'papel' as the df index name
    assert df_resultado_raw.index.name == 'papel'


###
### Check columns in '_raw' dataframe
###
lst1 = ['Cotação', 'P/L', 'P/VP', 'PSR', 'Div.Yield', 'P/Ativo', 'P/Cap.Giro',
       'P/EBIT', 'P/Ativ Circ.Liq', 'EV/EBIT', 'EV/EBITDA', 'Mrg Ebit',
       'Mrg. Líq.', 'Liq. Corr.', 'ROIC', 'ROE', 'Liq.2meses', 'Patrim. Líq',
       'Dív.Brut/ Patrim.', 'Cresc. Rec.5a']


@pytest.fixture(scope='session')
def _get_cols_raw(df_resultado_raw):
    chk = { x: True for x in df_resultado_raw.columns }
    return chk

@pytest.mark.parametrize('param', lst1)
def test_get_resultado_raw_has_col(_get_cols_raw, param):
    # GIVEN a 'resultado_raw' df
    # THEN  column names must be the HTML literal version
    my_chk = _get_cols_raw
    assert my_chk[param] == True


###
@pytest.fixture(name='df_resultado', scope='session')
def _get_resultado():
    df = resultado.get_resultado()
    return df


###
def test_get_resultado_len(df_resultado):
    # GIVEN a 'resultado' df
    # THEN  it must have '> 0' rows
    assert len(df_resultado) > 0


###
def test_get_resultado_index_name(df_resultado):
    # GIVEN a 'resultado' df
    # THEN  it must have 'papel' as the df index name
    assert df_resultado.index.name == 'papel'


###
### Check columns in final dataframe
###
lst2 = ['cotacao', 'pl', 'pvp', 'psr', 'dy', 'pa', 'pcg', 'pebit', 'pacl',
       'evebit', 'evebitda', 'mrgebit', 'mrgliq', 'roic', 'roe', 'liqc',
       'liq2m', 'patrliq', 'divbpatr', 'c5y']

@pytest.fixture(scope='session')
def _get_cols_final(df_resultado):
    chk = { x: True for x in df_resultado.columns }
    return chk

@pytest.mark.parametrize('param', lst2)
def test_get_resultado_has_col(_get_cols_final, param):
    # GIVEN a 'resultado' df
    # THEN  column names must be the final version
    my_chk = _get_cols_final
    assert my_chk[param] == True


