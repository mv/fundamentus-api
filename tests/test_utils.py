
from fundamentus import utils

import fundamentus
import pandas as pd
import pytest


###
def test_dt_iso8601_10_10():
    assert utils.dt_iso8601('10/10/2020') == '2020-10-10'

def test_dt_iso8601_10_01():
    assert utils.dt_iso8601('01/10/2020') == '2020-10-01'

def test_dt_iso8601_01_10():
    assert utils.dt_iso8601('10/01/2020') == '2020-01-10'


###
def test_from_pt_br_01():
    more_data = { 'col1': [ 11,21,31,41,51],
                  'col2': [ 12,22,32,42,52],
                  'col3': [ 13,23,33,43,53]}
    b = { 'data': [ '?tst','tst()','tst$./','tst tst','tst__' ]}
    b.update(more_data)
    a = { 'data': [ 'tst' ,'tst'  ,'tst'   ,'tst_tst','tst_'  ]}
    a.update(more_data)

    _before =  pd.DataFrame( b )
    _after  =  pd.DataFrame( a )

    _before['data'] = utils.from_pt_br(_before['data'])

    pd.testing.assert_frame_equal( _before, _after)


def test_from_pt_br_02():
    _before =  pd.DataFrame( { 'data': [ 'mês','Únicoúnico','imóvel','média adíção','tst b' ]} )
    _after  =  pd.DataFrame( { 'data': [ 'mes','Unicounico','imovel','media_adicao','tst_b' ]} )

    _before['data'] = utils.from_pt_br(_before['data'])

    pd.testing.assert_frame_equal(_before, _after)


###
def test_fmt_dec():
    more_data = { 'col1': [ 11,21],
                  'col2': [ 12,22],
                  'col3': [ 13,23]}
    b = { 'data': [ '45,56%','1.045,56%' ]}
    b.update(more_data)
    a = { 'data': [ '45.56%','1045.56%'  ]}
    a.update(more_data)

    _before = pd.DataFrame(b)
    _after  = pd.DataFrame(a)

    _before['data'] = utils.fmt_dec(_before['data'])
    pd.testing.assert_frame_equal(_before, _after)


###
def test_perc_to_float():
    more_data = { 'col1': [ 11,21],
                  'col2': [ 12,22],
                  'col3': [ 13,23]}
    b = { 'data': [ '45,56%','1.045,56%' ]}
    b.update(more_data)
    a = { 'data': [   0.4556, 10.4556    ]}
    a.update(more_data)

    _before = pd.DataFrame(b)
    _after  = pd.DataFrame(a)


    _before['data'] = utils.perc_to_float(_before['data'])
    pd.testing.assert_frame_equal(_before, _after)


###
@pytest.fixture(name='get_df', scope='session')
def _get_df_resultado():
    df = fundamentus.get_resultado()
    return df

def test_print_csv(capfd, get_df):
    # GIVEN calling 'print_csv()'
    # THEN  output must be a csv with many lines
    fundamentus.print_csv(get_df)
    out, err = capfd.readouterr()

    msg = out.split('\n')
    typ = type(msg)

    # output csv
    assert len(msg) > 5

def test_print_table(capfd, get_df):
    # GIVEN calling 'print_table()'
    # THEN  output must be a table with many lines
    fundamentus.print_table(get_df)
    out, err = capfd.readouterr()

    msg = out.split('\n')
    typ = type(msg)

    # output table
    assert len(msg) > 5


