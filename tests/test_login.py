import allure

from pages.login_page import LoginPage
from pages.home_page import HomePage
from urls import URL_MAIN_PAGE


class TestLogin:
    @allure.step("Проверка авторизации пользователя")
    def test_login(self, driver, create_user):
        login_page = LoginPage(driver)
        login_page.go_to_url(URL_MAIN_PAGE)
        # Войдем под созданным пользователем
        login_page.input_login_data(create_user['username'], create_user['password'])

        home_page = HomePage(driver)

        assert home_page.get_header_text() == 'Рецепты' and home_page.get_button_exit_text() == 'Выход'
