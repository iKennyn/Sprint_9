import random
import string

import allure


@allure.step("Рандомная генерация пользователя")
def generate_user_data():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    first_name = "Ivan_" + generate_random_string(3)
    last_name = "Ivanov_" + generate_random_string(5)
    username = "Ivan" + generate_random_string(3)
    email = generate_random_string(5) + "@yandex.ru"
    password = "1001_" + generate_random_string(3)

    # собираем тело запроса
    payload = {
        "first_name": first_name,
        "last_name": last_name,
        "username": username,
        "email": email,
        "password": password
    }
    return payload