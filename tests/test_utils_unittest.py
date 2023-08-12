
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

constants = [
            ("1.000.000", 1000000),
            ("1,23", 1.23),
            ("1.234,56", 1234.56),
            ("1,23%", 1.23e-2)
        ]

class Test_parse_numbers(unittest.TestCase):
    def test_numbers(self):
        for tuples in constants:
            self.assertAlmostEqual(
                utils.parse_number_in_portuguese_locale(tuples[0]),
                tuples[1])



if __name__ == '__main__':

    unittest.main()

