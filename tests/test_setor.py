
from fundamentus import setor

import pandas as pd
import pytest


###
@pytest.mark.parametrize(
    'param',[ pytest.param(20, id='fin' )
            , pytest.param(37, id='fin-diversos' )
#           , pytest.param(35, id='seg-rec' )
            , pytest.param(31, id='prev-seg')
            ])
def test_list_papel_setor__len(param):
    # GIVEN calling 'list_papel_setor()'
    # WHEN  'setor' is 35 or 38
    # THEN  list must contain more than on 'papel'
    lst = setor.list_papel_setor(param)
    assert len(lst) > 0


###
@pytest.mark.parametrize(
    'param',[ pytest.param( ['financeiro'  , 20], id='fin' )
            , pytest.param( ['fin-diversos', 37], id='fin-diversos' )
            , pytest.param( ['prev-seguros', 31], id='prev-seg')
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

    # output table: 46 lines
    assert len(msg) == 46


