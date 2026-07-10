import allure
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):
    @allure.step("Проверка заголовка главной страницы")
    def get_header_text(self):
        return self.get_text_from_element(HomePageLocators.HEADER)

    @allure.step("Проверка отображения кнопки 'Выход'")
    def get_button_exit_text(self):
        return self.get_text_from_element(HomePageLocators.EXIT_BUTTON)

    @allure.step("Клик на кнопку 'Создать рецепт'")
    def click_to_button_create_recipe(self):
        self.click_to_element(HomePageLocators.CREATE_RECIPE_BUTTON)
