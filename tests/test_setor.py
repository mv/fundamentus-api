
from fundamentus import setor

import pandas as pd
import pytest


###
@pytest.mark.parametrize(
    'param',[ pytest.param(35, id='fin' )
            , pytest.param(38, id='seg' )
            , pytest.param(38, id='prev')
            ])
def test_list_papel_setor__len(param):

    lst = setor.list_papel_setor(param)
    assert len(lst) > 0


###
@pytest.mark.parametrize(
    'param',[ pytest.param( ['financeiro' , 35], id='fin' )
            , pytest.param( ['seguros'    , 38], id='seg' )
            , pytest.param( ['previdencia', 38], id='prev')
            ])
def test_get_setor_id__setor(param):

    assert setor.get_setor_id(param[0]) == param[1]


###
def test_print_setores(capfd):
    setor.print_setores()
    out, err = capfd.readouterr()

    msg = out.split('\n')
    typ = type(msg)

    # output table: 51 lines
    assert len(msg) == 51


