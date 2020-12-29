
from fundamentus import utils

import pandas as pd
import unittest

class Test_dt_iso8601(unittest.TestCase):

    def test_dt_iso8601_10_10(self):
        assert utils.dt_iso8601('10/10/2020') == '2020-10-10'

    def test_dt_iso8601_10_01(self):
        assert utils.dt_iso8601('01/10/2020') == '2020-10-01'

    def test_dt_iso8601_01_10(self):
        assert utils.dt_iso8601('10/01/2020') == '2020-01-10'


class Test_from_pt_br(unittest.TestCase):

    def test_from_pt_br_01(self):
        _before =  pd.DataFrame( { 'data': [ '?tst','tst()','tst$./','tst tst','tst__' ]} )
        _after  =  pd.DataFrame( { 'data': [ 'tst' ,'tst'  ,'tst'   ,'tst_tst','tst_'  ]} )
        _test   = utils.from_pt_br(_before['data'])

        pd.testing.assert_frame_equal(_test.to_frame(), _after)


    def test_from_pt_br_02(self):
        _before =  pd.DataFrame( { 'data': [ 'mês','Únicoúnico','imóvel','média adíção','tst b' ]} )
        _after  =  pd.DataFrame( { 'data': [ 'mes','Unicounico','imovel','media_adicao','tst_b' ]} )
        _test   = utils.from_pt_br(_before['data'])

        pd.testing.assert_frame_equal(_test.to_frame(), _after)


if __name__ == '__main__':

    unittest.main()

