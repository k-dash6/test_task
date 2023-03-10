""" This file contains UI tests"""
import json
import requests

from data_for_tests.data_for_requests import REGISTER_DATA_RIGHT, REGISTER_DATA_WRONG, LOGIN_DATA_RIGHT, \
    LOGIN_DATA_WRONG, UPDATE_CREATE_DATA
from features.api.urls.urls import MainUrls
from features.ui.apps.element_actions import click_to_element, get_text_from_element
from features.ui.locators.locators import BaseLocators


def test_ui_list_users(driver_fixture):
    """ This test checks ui response matches api response for list users request """
    click_to_element(BaseLocators.LIST_USERS, driver_fixture)
    response = requests.get(MainUrls.LIST_USERS)

    code_ui = int(get_text_from_element(BaseLocators.RESPONSE_CODE, driver_fixture))
    response_output_ui = json.loads(get_text_from_element(BaseLocators.OUTPUT_RESPONSE, driver_fixture))

    assert response.status_code == code_ui, f"Code values from api and ui are not matches. " \
                                            f"UI: {code_ui}, API: {response.status_code}"
    assert response.json() == response_output_ui, f"Response from api and ui are not matches. " \
                                                  f"UI: {response_output_ui}, API: {response.json()}"


def test_ui_single_user(driver_fixture):
    """ This test checks ui response matches api response for single user request """
    click_to_element(BaseLocators.SINGLE_USER, driver_fixture)
    response = requests.get(MainUrls.SINGLE_USER)

    code_ui = int(get_text_from_element(BaseLocators.RESPONSE_CODE, driver_fixture))
    response_output_ui = json.loads(get_text_from_element(BaseLocators.OUTPUT_RESPONSE, driver_fixture))

    assert response.status_code == code_ui, f"Code values from api and ui are not matches. " \
                                            f"UI: {code_ui}, API: {response.status_code}"
    assert response.json() == response_output_ui, f"Response from api and ui are not matches. " \
                                                  f"UI: {response_output_ui}, API: {response.json()}"


def test_ui_single_user_not_found(driver_fixture):
    """ This test checks ui response matches api response for single user not found request """
    click_to_element(BaseLocators.SINGLE_USER_NOT_FOUND, driver_fixture)
    response = requests.get(MainUrls.SINGLE_USER_NOT_FOUND)

    code_ui = int(get_text_from_element(BaseLocators.RESPONSE_CODE, driver_fixture))
    response_output_ui = json.loads(get_text_from_element(BaseLocators.OUTPUT_RESPONSE, driver_fixture))

    assert response.status_code == code_ui, f"Code values from api and ui are not matches. " \
                                            f"UI: {code_ui}, API: {response.status_code}"
    assert response.json() == response_output_ui, f"Response from api and ui are not matches. " \
                                                  f"UI: {response_output_ui}, API: {response.json()}"


def test_ui_list_resource(driver_fixture):
    """ This test checks ui response matches api response for list resource request """
    click_to_element(BaseLocators.LIST_RESOURCE, driver_fixture)
    response = requests.get(MainUrls.LIST_RESOURCE)

    code_ui = int(get_text_from_element(BaseLocators.RESPONSE_CODE, driver_fixture))
    response_output_ui = json.loads(get_text_from_element(BaseLocators.OUTPUT_RESPONSE, driver_fixture))

    assert response.status_code == code_ui, f"Code values from api and ui are not matches. " \
                                            f"UI: {code_ui}, API: {response.status_code}"
    assert response.json() == response_output_ui, f"Response from api and ui are not matches. " \
                                                  f"UI: {response_output_ui}, API: {response.json()}"


def test_ui_single_resource(driver_fixture):
    """ This test checks ui response matches api response for single resource request """
    click_to_element(BaseLocators.SINGLE_RESOURCE, driver_fixture)
    response = requests.get(MainUrls.SINGLE_RESOURCE)

    code_ui = int(get_text_from_element(BaseLocators.RESPONSE_CODE, driver_fixture))
    response_output_ui = json.loads(get_text_from_element(BaseLocators.OUTPUT_RESPONSE, driver_fixture))

    assert response.status_code == code_ui, f"Code values from api and ui are not matches. " \
                                            f"UI: {code_ui}, API: {response.status_code}"
    assert response.json() == response_output_ui, f"Response from api and ui are not matches. " \
                                                  f"UI: {response_output_ui}, API: {response.json()}"


def test_ui_single_resource_not_found(driver_fixture):
    """ This test checks ui response matches api response for single resource not found request """
    click_to_element(BaseLocators.SINGLE_RESOURCE_NOT_FOUND, driver_fixture)
    response = requests.get(MainUrls.SINGLE_RESOURCE_NOT_FOUND)

    code_ui = int(get_text_from_element(BaseLocators.RESPONSE_CODE, driver_fixture))
    response_output_ui = json.loads(get_text_from_element(BaseLocators.OUTPUT_RESPONSE, driver_fixture))

    assert response.status_code == code_ui, f"Code values from api and ui are not matches. " \
                                            f"UI: {code_ui}, API: {response.status_code}"
    assert response.json() == response_output_ui, f"Response from api and ui are not matches. " \
                                                  f"UI: {response_output_ui}, API: {response.json()}"


def test_ui_create_user(driver_fixture):
    """ This test checks ui response codes matches api response for create user put request """
    click_to_element(BaseLocators.CREATE, driver_fixture)
    response = requests.post(MainUrls.CREATE_USER, data=UPDATE_CREATE_DATA)

    code_ui = int(get_text_from_element(BaseLocators.RESPONSE_CODE, driver_fixture))

    assert response.status_code == code_ui, f"Code values from api and ui are not matches. " \
                                            f"UI: {code_ui}, API: {response.status_code}"


def test_ui_update_user_put(driver_fixture, update_user_data):
    """ This test checks ui response codes matches api response for update user put request """
    click_to_element(BaseLocators.UPDATE_PUT, driver_fixture)
    response = requests.put(MainUrls.EDIT_USER, data=update_user_data)

    code_ui = int(get_text_from_element(BaseLocators.RESPONSE_CODE, driver_fixture))

    assert response.status_code == code_ui, f"Code values from api and ui are not matches. " \
                                            f"UI: {code_ui}, API: {response.status_code}"


def test_ui_update_user_patch(driver_fixture, update_user_data):
    """ This test checks ui response codes matches api response for update user patch request """
    click_to_element(BaseLocators.UPDATE_PATCH, driver_fixture)
    response = requests.patch(MainUrls.EDIT_USER, data=update_user_data)

    code_ui = int(get_text_from_element(BaseLocators.RESPONSE_CODE, driver_fixture))

    assert response.status_code == code_ui, f"Code values from api and ui are not matches. " \
                                            f"UI: {code_ui}, API: {response.status_code}"


def test_ui_delete_user(driver_fixture):
    """ This test checks ui response codes matches api response for delete user request """
    click_to_element(BaseLocators.DELETE, driver_fixture)
    response = requests.delete(MainUrls.EDIT_USER)

    code_ui = int(get_text_from_element(BaseLocators.RESPONSE_CODE, driver_fixture))

    assert response.status_code == code_ui, f"Code values from api and ui are not matches. " \
                                            f"UI: {code_ui}, API: {response.status_code}"


def test_ui_register_successful(driver_fixture):
    """ This test checks ui response matches api response for successful register request """
    click_to_element(BaseLocators.REGISTER_SUCCESSFUL, driver_fixture)
    response = requests.post(MainUrls.REGISTER, data=REGISTER_DATA_RIGHT)

    code_ui = int(get_text_from_element(BaseLocators.RESPONSE_CODE, driver_fixture))
    response_output_ui = json.loads(get_text_from_element(BaseLocators.OUTPUT_RESPONSE, driver_fixture))

    assert response.status_code == code_ui, f"Code values from api and ui are not matches. " \
                                            f"UI: {code_ui}, API: {response.status_code}"
    assert response.json() == response_output_ui, f"Response from api and ui are not matches. " \
                                                  f"UI: {response_output_ui}, API: {response.json()}"


def test_ui_register_unsuccessful(driver_fixture):
    """ This test checks ui response matches api response for unsuccessful register request """
    click_to_element(BaseLocators.REGISTER_UNSUCCESSFUL, driver_fixture)
    response = requests.post(MainUrls.REGISTER, data=REGISTER_DATA_WRONG)

    code_ui = int(get_text_from_element(BaseLocators.RESPONSE_CODE, driver_fixture))
    response_output_ui = json.loads(get_text_from_element(BaseLocators.OUTPUT_RESPONSE, driver_fixture))

    assert response.status_code == code_ui, f"Code values from api and ui are not matches. " \
                                            f"UI: {code_ui}, API: {response.status_code}"
    assert response.json() == response_output_ui, f"Response from api and ui are not matches. " \
                                                  f"UI: {response_output_ui}, API: {response.json()}"


def test_ui_login_successful(driver_fixture):
    """ This test checks ui response matches api response for successful login request """
    click_to_element(BaseLocators.LOGIN_SUCCESSFUL, driver_fixture)
    response = requests.post(MainUrls.LOGIN, data=LOGIN_DATA_RIGHT)

    code_ui = int(get_text_from_element(BaseLocators.RESPONSE_CODE, driver_fixture))
    response_output_ui = json.loads(get_text_from_element(BaseLocators.OUTPUT_RESPONSE, driver_fixture))

    assert response.status_code == code_ui, f"Code values from api and ui are not matches. " \
                                            f"UI: {code_ui}, API: {response.status_code}"
    assert response.json() == response_output_ui, f"Response from api and ui are not matches. " \
                                                  f"UI: {response_output_ui}, API: {response.json()}"


def test_ui_login_unsuccessful(driver_fixture):
    """ This test checks ui response matches api response for unsuccessful login request """
    click_to_element(BaseLocators.LOGIN_UNSUCCESSFUL, driver_fixture)
    response = requests.post(MainUrls.LOGIN, data=LOGIN_DATA_WRONG)

    code_ui = int(get_text_from_element(BaseLocators.RESPONSE_CODE, driver_fixture))
    response_output_ui = json.loads(get_text_from_element(BaseLocators.OUTPUT_RESPONSE, driver_fixture))

    assert response.status_code == code_ui, f"Code values from api and ui are not matches. " \
                                            f"UI: {code_ui}, API: {response.status_code}"
    assert response.json() == response_output_ui, f"Response from api and ui are not matches. " \
                                                  f"UI: {response_output_ui}, API: {response.json()}"


def test_ui_delayed_response(driver_fixture):
    """ This test checks ui response matches api response for delayed request """
    click_to_element(BaseLocators.DELAY, driver_fixture)
    response = requests.get(MainUrls.DELAY)

    code_ui = int(get_text_from_element(BaseLocators.RESPONSE_CODE, driver_fixture))
    response_output_ui = json.loads(get_text_from_element(BaseLocators.OUTPUT_RESPONSE, driver_fixture))

    assert response.status_code == code_ui, f"Code values from api and ui are not matches. " \
                                            f"UI: {code_ui}, API: {response.status_code}"
    assert response.json() == response_output_ui, f"Response from api and ui are not matches. " \
                                                  f"UI: {response_output_ui}, API: {response.json()}"
