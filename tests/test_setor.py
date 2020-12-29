
from fundamentus import setor

import pandas as pd


def test_get_setor_data():
    lst = setor.get_setor_data(35)
    assert len(lst) > 0


def test_get_setor_id():
    assert setor.get_setor_id('financeiro' ) == 35
    assert setor.get_setor_id('previdencia') == 38
    assert setor.get_setor_id('seguros'    ) == 38

def test_list_setor(capfd):
    setor.list_setor()
    out, err = capfd.readouterr()

    msg = out.split('\n')
    typ = type(msg)

    # output table: 51 lines
    assert len(msg) == 51


