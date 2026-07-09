import random
import string

import allure

from pages.base_page import BasePage
from locators.registration_page_locators import RegistrationPageLocators

class RegistrationPage(BasePage):

    @allure.step("Ввод имени пользователя")
    def enter_first_name(self, first_name):
        self.add_text_to_element(RegistrationPageLocators.FIRST_NAME_INPUT, first_name)

    @allure.step("Ввод фамилии пользователя")
    def enter_last_name(self, last_name):
        self.add_text_to_element(RegistrationPageLocators.LAST_NAME_INPUT, last_name)

    @allure.step("Ввод логина пользователя")
    def enter_username(self, username):
        self.add_text_to_element(RegistrationPageLocators.LOGIN_USERNAME_INPUT, username)

    @allure.step("Ввод email пользователя")
    def enter_email(self, email):
        self.add_text_to_element(RegistrationPageLocators.EMAIL_INPUT, email)

    @allure.step("Ввод пароля пользователя")
    def enter_password(self, password):
        self.add_text_to_element(RegistrationPageLocators.PASSWORD_INPUT, password)

    @allure.step("Клик на кнопку 'Создать аккаунт'")
    def click_create_account_button(self):
        self.click_to_element(RegistrationPageLocators.CREATE_ACCOUNT_BUTTON)

    def enter_user_data(self):
        data = self.generate_user_data()
        self.enter_first_name(data['first_name'])
        self.enter_last_name(data['last_name'])
        self.enter_username(data['username'])
        self.enter_email(data['email'])
        self.enter_password(data['password'])
        self.click_create_account_button()
        return data

    @staticmethod
    @allure.step("Рандомная генерация пользователя")
    def generate_user_data():
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        first_name = "Ivan_" + generate_random_string(3)
        last_name = "Ivanov_" + generate_random_string(5)
        username = "Ivan" + generate_random_string(3)
        email = generate_random_string(5) + "@yandex.ru"
        password = "1001_" + generate_random_string(3)

        # собираем тело запроса
        payload = {
            "first_name": first_name,
            "last_name": last_name,
            "username": username,
            "email": email,
            "password": password
        }
        print(payload)
        return payload
