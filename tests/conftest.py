#
# conftest:
#   - pytest shared fixtures
#   - shared fixtures come here:
#     - initial setup
#     - common tear down
#

import pytest

import fundamentus


@pytest.fixture()
def set_log_level():
    pass


@pytest.fixture()
def set_cachedir():

    ## Setup:
    pass

    yield   # this is where the testing happens

    ## Teardown:
    pass


