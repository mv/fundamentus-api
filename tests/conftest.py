#
# conftest:
#   - pytest shared fixtures
#   - shared fixtures come here:
#     - initial setup
#     - common tear down
#

import pytest

import fundamentus


# Scope:
#   - function < module < class < session
#   - scope of SETUP/TEARDOWN
#
@pytest.fixture(scope='session')
def set_log_level():
    pass


@pytest.fixture()
def set_cachedir():

    ## Setup:
    pass

    yield   # this is where the testing happens

    ## Teardown:
    pass


