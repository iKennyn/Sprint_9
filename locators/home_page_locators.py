from selenium.webdriver.common.by import By


class HomePageLocators:

    HEADER = (By.XPATH, "//h1[contains(text(), 'Рецепты')]")
    EXIT_BUTTON = (By.XPATH, "//a[contains(text(), 'Выход')]")
    CREATE_RECIPE_BUTTON = (By.XPATH, "//a[contains(text(), 'Создать рецепт')]")
