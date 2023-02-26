""" This file contains fixtures """

import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver_fixture():
    """ This fixture opens web driver """
    driver = webdriver.Chrome()
    driver.get("https://reqres.in/")
    yield driver
    driver.quit()
