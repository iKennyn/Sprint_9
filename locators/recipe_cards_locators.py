from selenium.webdriver.common.by import By


class RecipeCardsLocators:
    RECIPE_TITLE = (By.XPATH, "//h1[contains(@class, 'styles_single-card__title__2QMPq')]")

    DESCRIPTION_BLOCK = (By.XPATH, "//div[contains(@class, 'styles_description__g6e8v')]/div")