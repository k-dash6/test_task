""" This file contains actions with web elements """

from datetime import datetime, timedelta


def find_element(locator, driver):
    """ This function is to find web element """
    element = driver.find_element(*locator)
    driver.execute_script("return arguments[0].scrollIntoView();", element)
    return element


def click_to_element(locator, driver):
    """ This function is to click to web element """
    element = find_element(locator, driver)
    element.click()
    return element


def get_text_from_element(locator, driver):
    """ This function is to get text from web element """
    text = ''
    end_time = datetime.now() + timedelta(seconds=10)
    while datetime.now() < end_time:
        element = find_element(locator, driver)
        text = element.text
        if text != '':
            break
    return text
