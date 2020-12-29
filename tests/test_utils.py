
from fundamentus import utils

import unittest

import pandas as pd


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_dt_iso8601(self):
        assert utils.dt_iso8601('10/10/2020') == '2020-10-10'
        assert utils.dt_iso8601('01/10/2020') == '2020-10-01'
        assert utils.dt_iso8601('10/01/2020') == '2020-01-10'

    def test_dt_iso8601_10_10(self):
        assert utils.dt_iso8601('10/10/2020') == '2020-10-10'

    def test_dt_iso8601_10_01(self):
        assert utils.dt_iso8601('01/10/2020') == '2020-10-01'

    def test_dt_iso8601_01_10(self):
        assert utils.dt_iso8601('10/01/2020') == '2020-01-10'

    def test_from_pt_br_01(self):
        data =  {'before': [ '?tst','tst()','tst$./','tst tst','tst__' ],
                 'after' : [ 'tst' ,'tst'  ,'tst'   ,'tst_tst','tst_'  ],
                }
                #'before':  [ 'mês é a solução úÚnica íó' ]},
        df = pd.DataFrame(data)
        b = df['before']
        a = df['after']
        val = utils.from_pt_br(b) ## assert val == a ?
        assert True


if __name__ == '__main__':
    unittest.main()

