""" This file contains UI tests"""
import json

import pytest
import requests

from data_for_tests.data_for_requests import REGISTER_DATA_RIGHT, REGISTER_DATA_WRONG, LOGIN_DATA_RIGHT, \
    LOGIN_DATA_WRONG
from features.api.urls.urls import MainUrls
from features.ui.apps.element_actions import click_to_element, get_text_from_element
from features.ui.locators.locators import LIST_USERS, RESPONSE_CODE, OUTPUT_RESPONSE, DELAY, LOGIN_UNSUCCESSFUL, \
    LOGIN_SUCCESSFUL, REGISTER_UNSUCCESSFUL, REGISTER_SUCCESSFUL, DELETE, UPDATE_PATCH, UPDATE_PUT, CREATE, \
    SINGLE_RESOURCE_NOT_FOUND, SINGLE_RESOURCE, LIST_RESOURCE, SINGLE_USER_NOT_FOUND, SINGLE_USER


def test_ui_list_users(driver_fixture):
    """ This test checks ui response matches api response for list users request """
    click_to_element(LIST_USERS, driver_fixture)
    response = requests.get(MainUrls.LIST_USERS)

    code_ui = int(get_text_from_element(RESPONSE_CODE, driver_fixture))
    response_output_ui = json.loads(get_text_from_element(OUTPUT_RESPONSE, driver_fixture))

    assert response.status_code == code_ui, f"Code values from api and ui are not matches. " \
                                            f"UI: {code_ui}, API: {response.status_code}"
    assert response.json() == response_output_ui, f"Response from api and ui are not matches. " \
                                                  f"UI: {response_output_ui}, API: {response.json()}"


def test_ui_single_user(driver_fixture):
    """ This test checks ui response matches api response for single user request """
    click_to_element(SINGLE_USER, driver_fixture)
    response = requests.get(MainUrls.SINGLE_USER)

    code_ui = int(get_text_from_element(RESPONSE_CODE, driver_fixture))
    response_output_ui = json.loads(get_text_from_element(OUTPUT_RESPONSE, driver_fixture))

    assert response.status_code == code_ui, f"Code values from api and ui are not matches. " \
                                            f"UI: {code_ui}, API: {response.status_code}"
    assert response.json() == response_output_ui, f"Response from api and ui are not matches. " \
                                                  f"UI: {response_output_ui}, API: {response.json()}"


def test_ui_single_user_not_found(driver_fixture):
    """ This test checks ui response matches api response for single user not found request """
    click_to_element(SINGLE_USER_NOT_FOUND, driver_fixture)
    response = requests.get(MainUrls.SINGLE_USER_NOT_FOUND)

    code_ui = int(get_text_from_element(RESPONSE_CODE, driver_fixture))
    response_output_ui = json.loads(get_text_from_element(OUTPUT_RESPONSE, driver_fixture))

    assert response.status_code == code_ui, f"Code values from api and ui are not matches. " \
                                            f"UI: {code_ui}, API: {response.status_code}"
    assert response.json() == response_output_ui, f"Response from api and ui are not matches. " \
                                                  f"UI: {response_output_ui}, API: {response.json()}"


def test_ui_list_resource(driver_fixture):
    """ This test checks ui response matches api response for list resource request """
    click_to_element(LIST_RESOURCE, driver_fixture)
    response = requests.get(MainUrls.LIST_RESOURCE)

    code_ui = int(get_text_from_element(RESPONSE_CODE, driver_fixture))
    response_output_ui = json.loads(get_text_from_element(OUTPUT_RESPONSE, driver_fixture))

    assert response.status_code == code_ui, f"Code values from api and ui are not matches. " \
                                            f"UI: {code_ui}, API: {response.status_code}"
    assert response.json() == response_output_ui, f"Response from api and ui are not matches. " \
                                                  f"UI: {response_output_ui}, API: {response.json()}"


def test_ui_single_resource(driver_fixture):
    """ This test checks ui response matches api response for single resource request """
    click_to_element(SINGLE_RESOURCE, driver_fixture)
    response = requests.get(MainUrls.SINGLE_RESOURCE)

    code_ui = int(get_text_from_element(RESPONSE_CODE, driver_fixture))
    response_output_ui = json.loads(get_text_from_element(OUTPUT_RESPONSE, driver_fixture))

    assert response.status_code == code_ui, f"Code values from api and ui are not matches. " \
                                            f"UI: {code_ui}, API: {response.status_code}"
    assert response.json() == response_output_ui, f"Response from api and ui are not matches. " \
                                                  f"UI: {response_output_ui}, API: {response.json()}"


def test_ui_single_resource_not_found(driver_fixture):
    """ This test checks ui response matches api response for single resource not found request """
    click_to_element(SINGLE_RESOURCE_NOT_FOUND, driver_fixture)
    response = requests.get(MainUrls.SINGLE_RESOURCE_NOT_FOUND)

    code_ui = int(get_text_from_element(RESPONSE_CODE, driver_fixture))
    response_output_ui = json.loads(get_text_from_element(OUTPUT_RESPONSE, driver_fixture))

    assert response.status_code == code_ui, f"Code values from api and ui are not matches. " \
                                            f"UI: {code_ui}, API: {response.status_code}"
    assert response.json() == response_output_ui, f"Response from api and ui are not matches. " \
                                                  f"UI: {response_output_ui}, API: {response.json()}"


# @pytest.mark.parametrize("data", CREATE_USER_PARAMETERS)
# def test_ui_create_user(driver_fixture, data):
#     """ This test checks ui """
#     click_to_element(CREATE, driver_fixture)
#     code_ui = int(get_text_from_element(RESPONSE_CODE, driver_fixture))
#     response_output_ui = json.loads(get_text_from_element(OUTPUT_RESPONSE, driver_fixture))
#
#     response = requests.post(MainUrls.CREATE_USER, data=data)
#     assert response.status_code == code_ui
#     assert response.json() == response_output_ui


def test_ui_update_user_put(driver_fixture, update_user_data):
    """ This test checks ui response matches api response for update user put request """
    click_to_element(UPDATE_PUT, driver_fixture)
    response = requests.put(MainUrls.EDIT_USER, data=update_user_data)

    code_ui = int(get_text_from_element(RESPONSE_CODE, driver_fixture))
    response_output_ui = json.loads(get_text_from_element(OUTPUT_RESPONSE, driver_fixture))

    assert response.status_code == code_ui, f"Code values from api and ui are not matches. " \
                                            f"UI: {code_ui}, API: {response.status_code}"
    assert response.json() == response_output_ui, f"Response from api and ui are not matches. " \
                                                  f"UI: {response_output_ui}, API: {response.json()}"


def test_ui_update_user_patch(driver_fixture, update_user_data):
    """ This test checks ui response matches api response for update user patch request """
    click_to_element(UPDATE_PATCH, driver_fixture)
    response = requests.patch(MainUrls.EDIT_USER, data=update_user_data)

    code_ui = int(get_text_from_element(RESPONSE_CODE, driver_fixture))
    response_output_ui = json.loads(get_text_from_element(OUTPUT_RESPONSE, driver_fixture))

    assert response.status_code == code_ui, f"Code values from api and ui are not matches. " \
                                            f"UI: {code_ui}, API: {response.status_code}"
    assert response.json() == response_output_ui, f"Response from api and ui are not matches. " \
                                                  f"UI: {response_output_ui}, API: {response.json()}"


def test_ui_delete_user(driver_fixture):
    """ This test checks ui response matches api response for delete user request """
    click_to_element(DELETE, driver_fixture)
    response = requests.delete(MainUrls.EDIT_USER)

    code_ui = int(get_text_from_element(RESPONSE_CODE, driver_fixture))

    assert response.status_code == code_ui, f"Code values from api and ui are not matches. " \
                                            f"UI: {code_ui}, API: {response.status_code}"


def test_ui_register_successful(driver_fixture):
    """ This test checks ui response matches api response for successful register request """
    click_to_element(REGISTER_SUCCESSFUL, driver_fixture)
    response = requests.post(MainUrls.REGISTER, data=REGISTER_DATA_RIGHT)

    code_ui = int(get_text_from_element(RESPONSE_CODE, driver_fixture))
    response_output_ui = json.loads(get_text_from_element(OUTPUT_RESPONSE, driver_fixture))

    assert response.status_code == code_ui, f"Code values from api and ui are not matches. " \
                                            f"UI: {code_ui}, API: {response.status_code}"
    assert response.json() == response_output_ui, f"Response from api and ui are not matches. " \
                                                  f"UI: {response_output_ui}, API: {response.json()}"


def test_ui_register_unsuccessful(driver_fixture):
    """ This test checks ui response matches api response for unsuccessful register request """
    click_to_element(REGISTER_UNSUCCESSFUL, driver_fixture)
    response = requests.post(MainUrls.REGISTER, data=REGISTER_DATA_WRONG)

    code_ui = int(get_text_from_element(RESPONSE_CODE, driver_fixture))
    response_output_ui = json.loads(get_text_from_element(OUTPUT_RESPONSE, driver_fixture))

    assert response.status_code == code_ui, f"Code values from api and ui are not matches. " \
                                            f"UI: {code_ui}, API: {response.status_code}"
    assert response.json() == response_output_ui, f"Response from api and ui are not matches. " \
                                                  f"UI: {response_output_ui}, API: {response.json()}"


def test_ui_login_successful(driver_fixture):
    """ This test checks ui response matches api response for successful login request """
    click_to_element(LOGIN_SUCCESSFUL, driver_fixture)
    response = requests.post(MainUrls.LOGIN, data=LOGIN_DATA_RIGHT)

    code_ui = int(get_text_from_element(RESPONSE_CODE, driver_fixture))
    response_output_ui = json.loads(get_text_from_element(OUTPUT_RESPONSE, driver_fixture))

    assert response.status_code == code_ui, f"Code values from api and ui are not matches. " \
                                            f"UI: {code_ui}, API: {response.status_code}"
    assert response.json() == response_output_ui, f"Response from api and ui are not matches. " \
                                                  f"UI: {response_output_ui}, API: {response.json()}"


def test_ui_login_unsuccessful(driver_fixture):
    """ This test checks ui response matches api response for unsuccessful login request """
    click_to_element(LOGIN_UNSUCCESSFUL, driver_fixture)
    response = requests.post(MainUrls.LOGIN, data=LOGIN_DATA_WRONG)

    code_ui = int(get_text_from_element(RESPONSE_CODE, driver_fixture))
    response_output_ui = json.loads(get_text_from_element(OUTPUT_RESPONSE, driver_fixture))

    assert response.status_code == code_ui, f"Code values from api and ui are not matches. " \
                                            f"UI: {code_ui}, API: {response.status_code}"
    assert response.json() == response_output_ui, f"Response from api and ui are not matches. " \
                                                  f"UI: {response_output_ui}, API: {response.json()}"


def test_ui_delayed_response(driver_fixture):
    """ This test checks ui response matches api response for delayed request """
    click_to_element(DELAY, driver_fixture)
    response = requests.get(MainUrls.DELAY)

    code_ui = int(get_text_from_element(RESPONSE_CODE, driver_fixture))
    response_output_ui = json.loads(get_text_from_element(OUTPUT_RESPONSE, driver_fixture))

    assert response.status_code == code_ui, f"Code values from api and ui are not matches. " \
                                            f"UI: {code_ui}, API: {response.status_code}"
    assert response.json() == response_output_ui, f"Response from api and ui are not matches. " \
                                                  f"UI: {response_output_ui}, API: {response.json()}"
