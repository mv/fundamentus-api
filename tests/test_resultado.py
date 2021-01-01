
from fundamentus import resultado

import pytest
import pandas as pd



def test_get_resultado_raw_len():
    df = resultado.get_resultado_raw()
    assert len(df) > 0


###
cols = ['Cotação', 'P/L', 'P/VP', 'PSR', 'Div.Yield', 'P/Ativo', 'P/Cap.Giro',
       'P/EBIT', 'P/Ativ Circ.Liq', 'EV/EBIT', 'EV/EBITDA', 'Mrg Ebit',
       'Mrg. Líq.', 'Liq. Corr.', 'ROIC', 'ROE', 'Liq.2meses', 'Patrim. Líq',
       'Dív.Brut/ Patrim.', 'Cresc. Rec.5a']

@pytest.mark.parametrize('col_name', cols)
def test_get_resultado_raw_has_col(col_name):
    df = resultado.get_resultado_raw()
    assert col_name in list(df.columns)


###
def test_get_resultado_len():
    df = resultado.get_resultado()
    assert len(df) > 0


###
cols = ['cotacao', 'pl', 'pvp', 'psr', 'dy', 'pa', 'pcg', 'pebit', 'pacl',
       'evebit', 'evebitda', 'mrgebit', 'mrgliq', 'roic', 'roe', 'liqc',
       'liq2m', 'patrliq', 'divbpatr', 'c5y']

@pytest.mark.parametrize('col_name', cols)
def test_get_resultado_has_col(col_name):
    df = resultado.get_resultado()
    assert col_name in list(df.columns)


