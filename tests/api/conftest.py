import pytest
from data_for_tests.data_for_requests import UPDATE_USER_DATA


@pytest.fixture()
def update_user_data():
    """ This fixture returns data for update user """
    return UPDATE_USER_DATA
