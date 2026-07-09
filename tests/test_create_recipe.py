import allure

from pages.create_recipe_page import CreateRecipePage
from pages.home_page import HomePage
from pages.recipe_cards_page import RecipeCardsPage
from data import RECIPE_DATA


class TestCreateRecipe:
    @allure.step("Проверка регистрации нового рецепта")
    def test_create_recipe(self, driver, create_user, login):
        home_page = HomePage(driver)
        home_page.click_to_button_create_recipe()

        create_recipe_page = CreateRecipePage(driver)
        create_recipe_page.set_recipe_data("Батон.png")

        recipe_card = RecipeCardsPage(driver)
        assert (recipe_card.get_header_recipe_cards() == RECIPE_DATA['recipe_name'] and
                recipe_card.get_description_recipe_ingredients() == RECIPE_DATA['recipe_description'])
