from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    FIRST_NAME_INPUT = (By.XPATH, "//input[@type='text' and @name='first_name']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@type='text' and @name='last_name']")
    LOGIN_USERNAME_INPUT = (By.XPATH, "//input[@type='text' and @name='username']")
    EMAIL_INPUT = (By.XPATH, "//input[@type='text' and @name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password' and @name='password']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(@class, 'style_button_style_dark-blue') and contains(text(),"
                                       " 'Создать аккаунт')]")