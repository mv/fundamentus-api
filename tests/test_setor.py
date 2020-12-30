
from fundamentus import setor

import pandas as pd


def test_list_papel_setor():
    lst = setor.list_papel_setor(35)
    assert len(lst) > 0


def test_get_setor_id():
    assert setor.get_setor_id('financeiro' ) == 35
    assert setor.get_setor_id('previdencia') == 38
    assert setor.get_setor_id('seguros'    ) == 38

def test_print_setores(capfd):
    setor.print_setores()
    out, err = capfd.readouterr()

    msg = out.split('\n')
    typ = type(msg)

    # output table: 51 lines
    assert len(msg) == 51


