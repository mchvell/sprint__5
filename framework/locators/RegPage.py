from selenium.webdriver.common.by import By


class RegLocators:
    INPUTS = {
        "name": (By.XPATH, "//input[@name='name']"),
        "email": (By.XPATH, "//label[text()='Email']/following-sibling::input"),
        "password": (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    }

    END_REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")

    INCORRECT_PASSWORD = (By.XPATH, "//p[text()='Некорректный пароль']")

    AUTH_LINK = (By.XPATH, "//a[text()='Войти']")
