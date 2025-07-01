# Python Fundamentus


## 1. Bootstrap local Python virtual env

```bash
make
make show
```

    This: [Darwin 21.4.0]
    Virtualenv: [venv]
    Python Version: []


```bash
make venv
source venv/bin/activate
make show
```

    This: [Darwin 21.4.0]
    Virtualenv: [venv]
    Python Version: [Python 3.9.12]


## 2. Install/test dependencies

```bash
make req
make req-dev
make test
```

    ...
     tests/test_utils_unittest.py::Test_from_pt_br.test_from_pt_br_01 ✓                                                 99% █████████▉
     tests/test_utils_unittest.py::Test_from_pt_br.test_from_pt_br_02 ✓                                                100% ██████████

    Results (4.11s):
         103 passed


## 3. Install/test bash scripts

```bash
pip install fundamentus
make test-bash
```

    ...
    ###
    ### python3 examples/magic_formula.simple.py
    ###
    2022-04-24 12:43:54,280 [logging.log_init] INFO: LOGLEVEL=info

    ===
    === Count: Success = 9/9
    ===

            7.51 real        10.32 user         1.53 sys

