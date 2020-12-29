
from fundamentus import papel

import pandas as pd


def test_get_list_papel():
    lst = papel.get_list_papel()
    assert len(lst) > 10

def test_get_df_papel():

    cols = ['Papel', 'Nome Comercial', 'Razão Social']
    df = papel.get_df_papel()

    assert len(df) > 0
    assert list(df.columns) == cols

