from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pathlib import Path
import allure


class BasePage:
    ROOT_DIR = Path(__file__).parent.parent

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.wait = WebDriverWait(driver, self.timeout)

    @allure.step("Переход на страницу")
    def go_to_url(self, url):
        self.driver.get(url)

    @allure.step("Поиск элемента на странице")
    def find_element_with_wait(self, locator):
        self.wait.until(
            expected_conditions.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Клик по элементу")
    def click_to_element(self, locator):
        self.wait.until(
            expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step("Проверить видимость элемента")
    def is_element_visible(self, locator):
        try:
            return self.driver.find_element(*locator).is_displayed()
        except:
            return False

    @allure.step("Ввод текст")
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step("Получение текста")
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def get_image_path(self, filename: str) -> str:
        # Возвращает абсолютный путь к файлу из папки assets в виде строки
        root_dir = Path(__file__).resolve().parent.parent
        # Собираем путь до файла в папке assets
        file_path = root_dir / "assets" / filename
        return str(file_path)

    def lambda_func(self, condition):
        try:
            result = self.wait.until(condition)
            return result if result else ""  # Не возвращаем None
        except:
            return
