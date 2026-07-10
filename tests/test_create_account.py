import allure

from pages.login_page import LoginPage
from pages.registration_user_page import RegistrationPage
from urls import URL_MAIN_PAGE


class TestCreateAccount:
    @allure.step("Проверка регистрации нового пользователя")
    def test_create_account(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_url(URL_MAIN_PAGE)
        login_page.click_sign_up_button()
        login_page.get_login_form()

        registration_page = RegistrationPage(driver)
        registration_page.enter_user_data()

        assert login_page.get_header_login_page() == 'Войти на сайт' and login_page.get_login_form() == True
