
from fundamentus import papel

import pandas as pd
import pytest


@pytest.fixture()
def _get_list_papel():
    lst = papel.get_list_papel()
    return lst


def test_get_list_papel__len(_get_list_papel):
    assert len(_get_list_papel) > 10


lst = ['ABEV3','ITSA4','WEGE3']
@pytest.mark.parametrize('param', lst)
def test_get_list_papel__len(_get_list_papel, param):
    assert param in _get_list_papel


###
@pytest.fixture()
def _get_df_papel():
    df = papel.get_df_papel()
    return df


def test_get_df_papel__len(_get_df_papel):
    assert len(_get_df_papel) > 0


cols = ['Papel', 'Nome Comercial', 'Razão Social']

@pytest.mark.parametrize('param', cols)
def test_get_df_papel__col(_get_df_papel, param):
    assert param in list(_get_df_papel.columns)


