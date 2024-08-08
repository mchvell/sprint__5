from selenium.webdriver.common.by import By


class MainPageLocators:
    TABS = {
        "bread": (By.XPATH, "//span[text()='Булки']"),
        "sauce": (By.XPATH, "//span[text()='Соусы']"),
        "topping": (By.XPATH, "//span[text()='Начинки']")
    }

    TABS_HEADERS = {
        "bread": (By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10'][text()='Булки']"),
        "sauce": (By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10'][text()='Соусы']"),
        "topping": (By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10'][text()='Начинки']")
    }

    ENTER_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")