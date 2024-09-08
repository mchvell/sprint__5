from framework.pageObject.BasePage import BasePage
from framework.locators.ProfilePage import ProfilePageLocators as p


class ProfilePageHelper(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://stellarburgers.nomoreparties.site/account/profile"
        self.exit_button = p.EXIT_BUTTON

    def get_text_on_exit_button(self):
        return self.find_element(self.exit_button, 10).text

    def click_on_exit_button(self):
        return self.find_element(self.exit_button, 10).click()

