""" This file contains urls """


class MainUrls:
    """ This class contains urls for main page """
    MAIN = 'https://reqres.in/api'
    LIST_USERS = f"{MAIN}/users?page=2"
    SINGLE_USER = f"{MAIN}/users/2"
    SINGLE_USER_NOT_FOUND = f"{MAIN}/users/23"
    LIST_RESOURCE = f"{MAIN}/unknown"
    SINGLE_RESOURCE = f"{MAIN}/unknown/2"
    SINGLE_RESOURCE_NOT_FOUND = f"{MAIN}/unknown/23"
    CREATE_USER = f"{MAIN}/users"
    EDIT_USER = f"{MAIN}/users/2"
    REGISTER = f"{MAIN}/register"
    LOGIN = f"{MAIN}/login"
    DELAY = f"{MAIN}/users?delay=3"
