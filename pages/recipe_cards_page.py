import allure

from pages.base_page import BasePage
from locators.recipe_cards_locators import RecipeCardsLocators

class RecipeCardsPage(BasePage):
    @allure.step("Получить заголовок карточки рецепта")
    def get_header_recipe_cards(self):
        return self.get_text_from_element(RecipeCardsLocators.RECIPE_TITLE)

    @allure.step("Получить описание карточки рецепта")
    def get_description_recipe_ingredients(self):
        return self.get_text_from_element(RecipeCardsLocators.DESCRIPTION_BLOCK)
