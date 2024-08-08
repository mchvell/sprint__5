from framework.pageObject.BasePage import BasePage
from framework.locators.RegPage import RegLocators


class RegPageHelper(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://stellarburgers.nomoreparties.site/register"

        self.input_locators = RegLocators.INPUTS
        self.end_registration_button_locator = RegLocators.END_REGISTRATION_BUTTON
        self.incorrect_password_locator = RegLocators.INCORRECT_PASSWORD
        self.auth_link_locator = RegLocators.AUTH_LINK

    def fill_reg_form(self, **kwargs):
        for field, value in kwargs.items():
            locator = self.input_locators.get(field)
            self.find_element(locator, 10).send_keys(value)
        return self

    def submit_form(self):
        self.find_element(self.end_registration_button_locator, 10).click()

    def get_input_value(self, input_value):
        locator = self.input_locators.get(input_value)
        element = self.find_element(locator, 10)
        return element.get_attribute('value')

    def click_on_input(self, input):
        locator = self.input_locators.get(input)
        self.find_element(locator, 10).click()

    def click_on_auth_link(self):
        self.find_element(self.auth_link_locator, 10).click()

    def get_incorrect_password_text(self):
        return self.find_element(self.incorrect_password_locator, 10).text
