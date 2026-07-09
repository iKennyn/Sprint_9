import os
import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.registration_user_page import RegistrationPage
from urls import URL_MAIN_PAGE


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
    os.system("pkill -f Chrome")

@pytest.fixture(scope='function')
def create_user(driver):
    login_page = LoginPage(driver)
    login_page.go_to_url(URL_MAIN_PAGE)
    login_page.click_sign_up_button()

    registration_page = RegistrationPage(driver)
    data = registration_page.enter_user_data()
    return data


@pytest.fixture(scope='function')
def login(driver, create_user):
    user_data = create_user
    login_page = LoginPage(driver)
    login_page.go_to_url(URL_MAIN_PAGE)
    login_page.input_login_data(user_data['username'], user_data['password'])

