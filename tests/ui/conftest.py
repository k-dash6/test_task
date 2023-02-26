""" This file contains fixtures """

import pytest
from selenium import webdriver

from data_for_tests.data_for_requests import UPDATE_USER_DATA


@pytest.fixture(scope="function")
def driver_fixture():
    """ This fixture opens web driver """
    driver = webdriver.Chrome()
    driver.get("https://reqres.in/")
    yield driver
    driver.quit()


@pytest.fixture()
def update_user_data():
    """ This fixture returns data for update user """
    return UPDATE_USER_DATA
