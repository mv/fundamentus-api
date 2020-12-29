
from fundamentus import utils

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_dt_iso8601(self):

        assert utils.dt_iso8601('10/10/2020') == '2020-10-10'
        assert utils.dt_iso8601('01/10/2020') == '2020-10-01'
        assert utils.dt_iso8601('10/01/2020') == '2020-01-10'


if __name__ == '__main__':
    unittest.main()

