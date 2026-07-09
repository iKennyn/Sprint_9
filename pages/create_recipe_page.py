import allure
from data import RECIPE_DATA
from pages.base_page import BasePage
from locators.create_recipe_locators import CreateRecipeLocators


class CreateRecipePage(BasePage):
    @allure.step("Ввод названия рецепта")
    def input_recipe_name(self, recipe_name):
        self.add_text_to_element(CreateRecipeLocators.RECIPE_NAME_INPUT, recipe_name)

    @allure.step("Выключение тэга 'Ужин'")
    def click_tags(self):
        self.click_to_element(CreateRecipeLocators.TAGS_PURPLE)

    @allure.step("Ввод ингредиента")
    def input_ingredients(self, ingredients):
        self.add_text_to_element(CreateRecipeLocators.INGREDIENTS_INPUT, ingredients)

    @allure.step("Выбор ингредиента 'Батон'")
    def click_ingredients_loaf(self):
        self.click_to_element(CreateRecipeLocators.DROPDOWN_LOAF)

    @allure.step("Ввод веса ингредиента")
    def input_weight(self, weight):
        self.add_text_to_element(CreateRecipeLocators.WEIGHTS_INPUT, weight)

    @allure.step("Клин 'Добавить ингредиент'")
    def click_add_ingredient(self):
        self.click_to_element(CreateRecipeLocators.ADD_INGREDIENT_BUTTON)

    @allure.step("Ввод времени приготовления")
    def input_preparation_time(self, preparation_time):
        self.add_text_to_element(CreateRecipeLocators.PREPARATION_TIME_INPUT, preparation_time)

    @allure.step("Заполнить описание рецепта")
    def input_recipe_description(self, recipe_description):
        self.add_text_to_element(CreateRecipeLocators.RECIPE_DESCRIPTION, recipe_description)

    @allure.step("Клик по кнопке 'Создать рецепт'")
    def click_create_recipe(self):
        self.click_to_element(CreateRecipeLocators.CREATE_RECIPE_BUTTON)

    @allure.step("Заполнить описание рецепта")
    def set_recipe_data(self, filename):
        self.input_recipe_name(RECIPE_DATA['recipe_name'])
        self.click_tags()
        self.input_ingredients(RECIPE_DATA['ingredient'])
        self.click_ingredients_loaf()
        self.input_weight(RECIPE_DATA['weight'])
        self.click_add_ingredient()
        self.input_preparation_time(RECIPE_DATA['preparation_time'])
        self.input_recipe_description(RECIPE_DATA['recipe_description'])
        self.upload_image(filename)
        self.click_create_recipe()

    @allure.step("Загрузить изображение рецепта")
    def upload_image(self, filename: str) -> None:
        #Загружает изображение из папки assets
        image_path = self.get_image_path(filename)
        file_input = self.find_element_with_wait(CreateRecipeLocators.UPLOAD_FILE)
        file_input.send_keys(image_path)
