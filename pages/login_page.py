import allure

from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    @allure.step("Заполнение формы авторизации пользователя")
    def input_login_data(self, username, password, max_attempts=5):
        for attempt in range(max_attempts):
            # Заполняем поля
            self.add_text_to_element(LoginPageLocators.LOGIN_SET, username)
            self.add_text_to_element(LoginPageLocators.PASSWORD_SET, password)
            # Кликаем на кнопку "Войти"
            self.click_to_element(LoginPageLocators.ENTER_BUTTON)
            #Проверяем alert
            if self.close_alert_if_present():
                if attempt < max_attempts - 1:
                    self.driver.refresh()
                    continue
                else:
                    raise AssertionError(f"Не удалось войти после {max_attempts} попыток")
            else:
                return True
        return False

    @allure.step("Клик по кнопке 'Создать аккаунт'")
    def click_sign_up_button(self):
        self.click_to_element(LoginPageLocators.SIGN_UP_BUTTON)

    @allure.step("Поиск заголовка страницы 'Авторизации'")
    def get_header_login_page(self):
        return self.get_text_from_element(LoginPageLocators.HEADER_LOGIN_PAGE)

    @allure.step("Проверка отображения формы авторизации")
    def get_login_form(self):
        element = self.element_of_visibility(LoginPageLocators.LOGIN_SET and LoginPageLocators.PASSWORD_SET)
        return element is not None
