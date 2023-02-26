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
from parameterization.create_user_parameters import CREATE_USER_PARAMETERS
from tests.api.conftest import update_user_data


def test_ui_list_users(driver_fixture):
    """ This test checks ui """
    click_to_element(LIST_USERS, driver_fixture)
    code_ui = int(get_text_from_element(RESPONSE_CODE, driver_fixture))
    response_output_ui = json.loads(get_text_from_element(OUTPUT_RESPONSE, driver_fixture))

    response = requests.get(MainUrls.LIST_USERS)
    assert response.status_code == code_ui
    assert response.json() == response_output_ui


def test_ui_single_user(driver_fixture):
    """ This test checks ui """
    click_to_element(SINGLE_USER, driver_fixture)
    code_ui = int(get_text_from_element(RESPONSE_CODE, driver_fixture))
    response_output_ui = json.loads(get_text_from_element(OUTPUT_RESPONSE, driver_fixture))

    response = requests.get(MainUrls.SINGLE_USER)
    assert response.status_code == code_ui
    assert response.json() == response_output_ui


def test_ui_single_user_not_found(driver_fixture):
    """ This test checks ui """
    click_to_element(SINGLE_USER_NOT_FOUND, driver_fixture)
    code_ui = int(get_text_from_element(RESPONSE_CODE, driver_fixture))
    response_output_ui = json.loads(get_text_from_element(OUTPUT_RESPONSE, driver_fixture))

    response = requests.get(MainUrls.SINGLE_USER_NOT_FOUND)
    assert response.status_code == code_ui
    assert response.json() == response_output_ui


def test_ui_list_resource(driver_fixture):
    """ This test checks ui """
    click_to_element(LIST_RESOURCE, driver_fixture)
    code_ui = int(get_text_from_element(RESPONSE_CODE, driver_fixture))
    response_output_ui = json.loads(get_text_from_element(OUTPUT_RESPONSE, driver_fixture))

    response = requests.get(MainUrls.LIST_RESOURCE)
    assert response.status_code == code_ui
    assert response.json() == response_output_ui


def test_ui_single_resource(driver_fixture):
    """ This test checks ui """
    click_to_element(SINGLE_RESOURCE, driver_fixture)
    code_ui = int(get_text_from_element(RESPONSE_CODE, driver_fixture))
    response_output_ui = json.loads(get_text_from_element(OUTPUT_RESPONSE, driver_fixture))

    response = requests.get(MainUrls.SINGLE_RESOURCE)
    assert response.status_code == code_ui
    assert response.json() == response_output_ui


def test_ui_single_resource_not_found(driver_fixture):
    """ This test checks ui """
    click_to_element(SINGLE_RESOURCE_NOT_FOUND, driver_fixture)
    code_ui = int(get_text_from_element(RESPONSE_CODE, driver_fixture))
    response_output_ui = json.loads(get_text_from_element(OUTPUT_RESPONSE, driver_fixture))

    response = requests.get(MainUrls.SINGLE_RESOURCE_NOT_FOUND)
    assert response.status_code == code_ui
    assert response.json() == response_output_ui


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


def test_ui_update_user_put(driver_fixture):
    """ This test checks ui """
    click_to_element(UPDATE_PUT, driver_fixture)
    code_ui = int(get_text_from_element(RESPONSE_CODE, driver_fixture))
    response_output_ui = json.loads(get_text_from_element(OUTPUT_RESPONSE, driver_fixture))

    response = requests.put(MainUrls.EDIT_USER, data=update_user_data)
    assert response.status_code == code_ui
    assert response.json() == response_output_ui


def test_ui_update_user_patch(driver_fixture):
    """ This test checks ui """
    click_to_element(UPDATE_PATCH, driver_fixture)
    code_ui = int(get_text_from_element(RESPONSE_CODE, driver_fixture))
    response_output_ui = json.loads(get_text_from_element(OUTPUT_RESPONSE, driver_fixture))

    response = requests.patch(MainUrls.EDIT_USER, data=update_user_data)
    assert response.status_code == code_ui
    assert response.json() == response_output_ui


def test_ui_delete_user(driver_fixture):
    """ This test checks ui """
    click_to_element(DELETE, driver_fixture)
    code_ui = int(get_text_from_element(RESPONSE_CODE, driver_fixture))

    response = requests.delete(MainUrls.EDIT_USER)
    assert response.status_code == code_ui


def test_ui_register_successful(driver_fixture):
    """ This test checks ui """
    click_to_element(REGISTER_SUCCESSFUL, driver_fixture)
    code_ui = int(get_text_from_element(RESPONSE_CODE, driver_fixture))
    response_output_ui = json.loads(get_text_from_element(OUTPUT_RESPONSE, driver_fixture))

    response = requests.post(MainUrls.REGISTER, data=REGISTER_DATA_RIGHT)
    assert response.status_code == code_ui
    assert response.json() == response_output_ui


def test_ui_register_unsuccessful(driver_fixture):
    """ This test checks ui """
    click_to_element(REGISTER_UNSUCCESSFUL, driver_fixture)
    code_ui = int(get_text_from_element(RESPONSE_CODE, driver_fixture))
    response_output_ui = json.loads(get_text_from_element(OUTPUT_RESPONSE, driver_fixture))

    response = requests.post(MainUrls.REGISTER, data=REGISTER_DATA_WRONG)
    assert response.status_code == code_ui
    assert response.json() == response_output_ui


def test_ui_login_successful(driver_fixture):
    """ This test checks ui """
    click_to_element(LOGIN_SUCCESSFUL, driver_fixture)
    code_ui = int(get_text_from_element(RESPONSE_CODE, driver_fixture))
    response_output_ui = json.loads(get_text_from_element(OUTPUT_RESPONSE, driver_fixture))

    response = requests.post(MainUrls.LOGIN, data=LOGIN_DATA_RIGHT)
    assert response.status_code == code_ui
    assert response.json() == response_output_ui


def test_ui_login_unsuccessful(driver_fixture):
    """ This test checks ui """
    click_to_element(LOGIN_UNSUCCESSFUL, driver_fixture)
    code_ui = int(get_text_from_element(RESPONSE_CODE, driver_fixture))
    response_output_ui = json.loads(get_text_from_element(OUTPUT_RESPONSE, driver_fixture))

    response = requests.post(MainUrls.LOGIN, data=LOGIN_DATA_WRONG)
    assert response.status_code == code_ui
    assert response.json() == response_output_ui


def test_ui_delayed_response(driver_fixture):
    """ This test checks ui """
    click_to_element(DELAY, driver_fixture)
    code_ui = int(get_text_from_element(RESPONSE_CODE, driver_fixture))

    response_output_ui = get_text_from_element(OUTPUT_RESPONSE, driver_fixture)
    response_output_ui = json.loads(response_output_ui)

    response = requests.get(MainUrls.DELAY)
    assert response.status_code == code_ui
    assert response.json() == response_output_ui
