""" This file contains locators """
from selenium.webdriver.common.by import By


class BaseLocators:
    # Requests buttons
    LIST_USERS = (By.XPATH, "//a[contains(text(),'List users')]")
    SINGLE_USER = (By.XPATH, "//a[contains(text(),'Single user')]")
    SINGLE_USER_NOT_FOUND = (By.XPATH, "//a[contains(text(),'Single user not found')]")
    LIST_RESOURCE = (By.XPATH, "//a[contains(text(),'List <resource>')]")
    SINGLE_RESOURCE = (By.XPATH, "//a[contains(text(),'Single <resource>')]")
    SINGLE_RESOURCE_NOT_FOUND = (By.XPATH, "//a[contains(text(),'Single <resource> not found')]")
    CREATE = (By.XPATH, "//a[contains(text(),'Create')]")
    UPDATE_PUT = (By.XPATH, "//li[@data-id='put']/a[contains(text(),'Update')]")
    UPDATE_PATCH = (By.XPATH, "//li[@data-id='patch']/a[contains(text(),'Update')]")
    DELETE = (By.XPATH, "//a[contains(text(),'Delete')]")
    REGISTER_SUCCESSFUL = (By.XPATH, "//a[contains(text(),'Register - successful')]")
    REGISTER_UNSUCCESSFUL = (By.XPATH, "//a[contains(text(),'Register - unsuccessful')]")
    LOGIN_SUCCESSFUL = (By.XPATH, "//a[contains(text(),'Login - successful')]")
    LOGIN_UNSUCCESSFUL = (By.XPATH, "//a[contains(text(),'Login - unsuccessful')]")
    DELAY = (By.XPATH, "//a[contains(text(),'Delayed response')]")

    # Panels
    OUTPUT_RESPONSE = (By.XPATH, "//pre[@data-key='output-response']")
    RESPONSE_CODE = (By.CLASS_NAME, "response-code")
