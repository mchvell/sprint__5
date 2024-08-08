from framework.pageObject.BasePage import BasePage
from framework.locators.AuthPage import AuthLocators


class AuthPageHelper(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://stellarburgers.nomoreparties.site/login"
        self.input_locators = AuthLocators.INPUTS
        self.enter_button_locator = AuthLocators.ENTER_BUTTON
        self.link_locators = AuthLocators.LINKS

    # правки после код ревью – упростил метод
    def fill_auth_form(self, **kwargs):
        for field, value in kwargs.items():
            locator = self.input_locators.get(field)
            self.find_element(locator, 10).send_keys(value)
        return self

    def click_enter_button(self):
        self.find_element(self.enter_button_locator, 10).click()

    def click_link(self, link_name):
        link_locator = self.link_locators.get(link_name)
        return self.find_element(link_locator, 10).click()

