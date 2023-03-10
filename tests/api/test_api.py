""" This file contains API tests"""
import pytest
import requests

from parameterization.create_user_parameters import CREATE_USER_PARAMETERS
from data_for_tests.data_for_requests import REGISTER_DATA_RIGHT, REGISTER_DATA_WRONG, \
    LOGIN_DATA_RIGHT, LOGIN_DATA_WRONG
from features.api.urls.urls import MainUrls


def test_get_list_users():
    """ This test checks list users request """
    response = requests.get(MainUrls.LIST_USERS)
    assert response.status_code == 200, f"Not expected code value: {response.status_code}. Expected: 200"


def test_get_single_user():
    """ This test checks single user request """
    response = requests.get(MainUrls.SINGLE_USER)
    assert response.status_code == 200, f"Not expected code value: {response.status_code}. Expected: 200"


def test_get_single_user_not_found():
    """ This test checks single user not found request """
    response = requests.get(MainUrls.SINGLE_USER_NOT_FOUND)
    assert response.status_code == 404, f"Not expected code value: {response.status_code}. Expected: 404"


def test_get_list_resource():
    """ This test checks list resource request """
    response = requests.get(MainUrls.LIST_RESOURCE)
    assert response.status_code == 200, f"Not expected code value: {response.status_code}. Expected: 200"


def test_get_single_resource():
    """ This test checks  single resource request """
    response = requests.get(MainUrls.SINGLE_RESOURCE)
    assert response.status_code == 200, f"Not expected code value: {response.status_code}. Expected: 200"


def test_get_single_resource_not_found():
    """ This test checks single resource not found request """
    response = requests.get(MainUrls.SINGLE_RESOURCE_NOT_FOUND)
    assert response.status_code == 404, f"Not expected code value: {response.status_code}. Expected: 404"


@pytest.mark.parametrize("data", CREATE_USER_PARAMETERS)
def test_create_user(data):
    """ This test checks create user request """
    response = requests.post(MainUrls.CREATE_USER, data=data)
    assert response.status_code == 201, f"Not expected code value: {response.status_code}. Expected: 201"
    assert response.json()["name"] == data["name"], f"Name from response is not match with entered"
    assert response.json()["job"] == data["job"], f"Job from response is not match with entered"


def test_update_user_put(update_user_data):
    """ This test checks update user put request """
    response = requests.put(MainUrls.EDIT_USER, data=update_user_data)
    assert response.status_code == 200, f"Not expected code value: {response.status_code}. Expected: 200"


def test_update_user_patch(update_user_data):
    """ This test checks update user patch request """
    response = requests.patch(MainUrls.EDIT_USER, data=update_user_data)
    assert response.status_code == 200, f"Not expected code value: {response.status_code}. Expected: 200"


def test_delete_user():
    """ This test checks delete user request """
    response = requests.delete(MainUrls.EDIT_USER)
    assert response.status_code == 204, f"Not expected code value: {response.status_code}. Expected: 204"


def test_register_successful():
    """ This test checks successful register request """
    response = requests.post(MainUrls.REGISTER, data=REGISTER_DATA_RIGHT)
    assert response.status_code == 200, f"Not expected code value: {response.status_code}. Expected: 200"
    assert 'token' in response.json(), f"No token in response"


def test_register_unsuccessful():
    """ This test checks unsuccessful register request """
    response = requests.post(MainUrls.REGISTER, data=REGISTER_DATA_WRONG)
    assert response.status_code == 400, f"Not expected code value: {response.status_code}. Expected: 400"
    assert 'error' in response.json(), f"No error in response"


def test_login_successful():
    """ This test checks successful login request """
    response = requests.post(MainUrls.LOGIN, data=LOGIN_DATA_RIGHT)
    assert response.status_code == 200, f"Not expected code value: {response.status_code}. Expected: 200"
    assert 'token' in response.json(), f"No token in response"


def test_login_unsuccessful():
    """ This test checks unsuccessful login request """
    response = requests.post(MainUrls.LOGIN, data=LOGIN_DATA_WRONG)
    assert response.status_code == 400, f"Not expected code value: {response.status_code}. Expected: 400"
    assert 'error' in response.json(), f"No error in response"


def test_delayed_response():
    """ This test checks delay request """
    response = requests.get(MainUrls.DELAY)
    assert response.status_code == 200, f"Not expected code value: {response.status_code}. Expected: 200"
