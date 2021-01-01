
from fundamentus import resultado

import pytest
import pandas as pd

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


@pytest.fixture()
def _get_resultado_raw():
    df = resultado.get_resultado_raw()
    return df


###
def test_get_resultado_raw_len(_get_resultado_raw):
    assert len(_get_resultado_raw) > 0


###
def test_get_resultado_raw_index_name(_get_resultado_raw):
    assert _get_resultado_raw.index.name == 'papel'


###
### Check columns in '_raw' dataframe
###
lst1 = ['Cotação', 'P/L', 'P/VP', 'PSR', 'Div.Yield', 'P/Ativo', 'P/Cap.Giro',
       'P/EBIT', 'P/Ativ Circ.Liq', 'EV/EBIT', 'EV/EBITDA', 'Mrg Ebit',
       'Mrg. Líq.', 'Liq. Corr.', 'ROIC', 'ROE', 'Liq.2meses', 'Patrim. Líq',
       'Dív.Brut/ Patrim.', 'Cresc. Rec.5a']

@pytest.fixture()
def _get_cols_raw(_get_resultado_raw):
    chk = { x: True for x in _get_resultado_raw.columns }
    return chk

@pytest.mark.parametrize('param', lst1)
def test_get_resultado_raw_has_col(_get_cols_raw, param):
    my_chk = _get_cols_raw
    assert my_chk[param] == True


###
@pytest.fixture()
def _get_resultado():
    df = resultado.get_resultado()
    return df


###
def test_get_resultado_len():
    df = resultado.get_resultado()
    assert len(df) > 0


###
def test_get_resultado_index_name():
    df = resultado.get_resultado()
    assert df.index.name == 'papel'


###
### Check columns in final dataframe
###
lst2 = ['cotacao', 'pl', 'pvp', 'psr', 'dy', 'pa', 'pcg', 'pebit', 'pacl',
       'evebit', 'evebitda', 'mrgebit', 'mrgliq', 'roic', 'roe', 'liqc',
       'liq2m', 'patrliq', 'divbpatr', 'c5y']

@pytest.fixture()
def _get_cols_final(_get_resultado):
    chk = { x: True for x in _get_resultado.columns }
    return chk

@pytest.mark.parametrize('param', lst2)
def test_get_resultado_has_col(_get_cols_final, param):
    my_chk = _get_cols_final
    assert my_chk[param] == True


