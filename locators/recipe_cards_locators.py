from selenium.webdriver.common.by import By


class RecipeCardsLocators:
    RECIPE_TITLE = (By.XPATH, "//div[contains(@class, 'styles_single-card__header-info')]/h1")

    DESCRIPTION_BLOCK = (By.XPATH, "//div[contains(@class, 'styles_description__g6e8v')]/div")