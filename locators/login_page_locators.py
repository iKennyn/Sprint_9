from selenium.webdriver.common.by import By


class LoginPageLocators:

    HEADER_LOGIN_PAGE = (By.XPATH, "//h1[text()='Войти на сайт']")
    LOGIN_SET = (By.XPATH, "//input[@name='email']")
    PASSWORD_SET = (By.XPATH, "//input[@name='password']")
    ENTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    SIGN_UP_BUTTON = (By.XPATH, "//a[contains(text(), 'Создать аккаунт')]")

    LOGIN_FORM = (By.XPATH, "//form[contains(@class, 'styles_form') and .//input[@name='email'] "
                            "and .//input[@name='password']]")
