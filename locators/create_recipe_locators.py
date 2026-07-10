from selenium.webdriver.common.by import By


class CreateRecipeLocators:

    RECIPE_NAME_INPUT = (By.XPATH, "//input[contains(@class, 'styles_inputField')]")
    TAGS_PURPLE = (By.XPATH, "//button[@style='background-color: purple;']")
    INGREDIENTS_INPUT = (By.XPATH, "//input[contains(@class, 'styles_ingredientsInput')]")
    DROPDOWN_LOAF = (By.XPATH, "//div[contains(text(), 'батон')]")
    WEIGHTS_INPUT = (By.XPATH, "//input[contains(@class, 'styles_ingredientsAmountValue')]")
    ADD_INGREDIENT_BUTTON = (By.XPATH, "//div[contains(text(), 'Добавить ингредиент')]")
    PREPARATION_TIME_INPUT = (By.XPATH, "//div[contains(@class, 'styles_cookingTime')]//input")
    RECIPE_DESCRIPTION = (By.XPATH, "//textarea[contains(@class, 'styles_textareaField') and @rows='8']")
    UPLOAD_FILE = (By.CSS_SELECTOR, "input[type='file']")
    CREATE_RECIPE_BUTTON = (By.XPATH, "//button[contains(text(), 'Создать рецепт')]")
