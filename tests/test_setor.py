
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
    # GIVEN calling 'list_papel_setor()'
    # WHEN  'setor' is 35 or 38
    # THEN  list must contain more than on 'papel'
    lst = setor.list_papel_setor(param)
    assert len(lst) > 0


###
@pytest.mark.parametrize(
    'param',[ pytest.param( ['financeiro' , 35], id='fin' )
            , pytest.param( ['seguros'    , 38], id='seg' )
            , pytest.param( ['previdencia', 38], id='prev')
            ])
def test_get_setor_id__setor(param):
    # GIVEN calling 'get_setor_id()'
    # WHEN  'setor' is called by name
    # THEN  result must the correct setor_id
    assert setor.get_setor_id(param[0]) == param[1]


###
def test_print_setores(capfd):
    # GIVEN calling 'print_setores()'
    # THEN  output must be a table with many lines
    setor.print_setores()
    out, err = capfd.readouterr()

    msg = out.split('\n')
    typ = type(msg)

    # output table: 51 lines
    assert len(msg) == 51


