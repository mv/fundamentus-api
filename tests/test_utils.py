
from fundamentus import utils

import pandas as pd


def test_dt_iso8601_10_10():
    assert utils.dt_iso8601('10/10/2020') == '2020-10-10'

def test_dt_iso8601_10_01():
    assert utils.dt_iso8601('01/10/2020') == '2020-10-01'

def test_dt_iso8601_01_10():
    assert utils.dt_iso8601('10/01/2020') == '2020-01-10'



def test_from_pt_br_01():
    _before =  pd.DataFrame( { 'data': [ '?tst','tst()','tst$./','tst tst','tst__' ]} )
    _after  =  pd.DataFrame( { 'data': [ 'tst' ,'tst'  ,'tst'   ,'tst_tst','tst_'  ]} )
    _test   = utils.from_pt_br(_before['data'])

    pd.testing.assert_frame_equal(_test.to_frame(), _after)


def test_from_pt_br_02():
    _before =  pd.DataFrame( { 'data': [ 'mês','Únicoúnico','imóvel','média adíção','tst b' ]} )
    _after  =  pd.DataFrame( { 'data': [ 'mes','Unicounico','imovel','media_adicao','tst_b' ]} )
    _test   = utils.from_pt_br(_before['data'])

    pd.testing.assert_frame_equal(_test.to_frame(), _after)



def test_fmt_dec():
    _before =  pd.DataFrame( { 'data': [ '45,56%','1.045,56%' ]} )
    _after  =  pd.DataFrame( { 'data': [ '45.56%','1045.56%' ]} )
    _test   = utils.fmt_dec(_before['data'])

    pd.testing.assert_frame_equal(_test.to_frame(), _after)



def test_perc_to_float():
    _before =  pd.DataFrame( { 'data': [ '45,56%', '1.045,56%' ]} )
    _after  =  pd.DataFrame( { 'data': [   0.4556, 10.4556     ]} )
    _test   = utils.perc_to_float(_before['data'])

    pd.testing.assert_frame_equal(_test.to_frame(), _after)


