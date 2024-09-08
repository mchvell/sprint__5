from framework.pageObject.BasePage import BasePage
from framework.locators.MainPage import MainPageLocators


class MainPageHelper(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.tab_locators = MainPageLocators.TABS
        self.tab_header_locators = MainPageLocators.TABS_HEADERS
        self.enter_button_locator = MainPageLocators.ENTER_BUTTON

    def click_on_enter_button(self):
        self.find_element(self.enter_button_locator, 10).click()

    def set_tab(self, tab):
        tab_locator = self.tab_locators.get(tab)
        return self.find_element(tab_locator, 10).click()

    def get_tab_header_text(self, tab):
        header_locator = self.tab_header_locators.get(tab)
        header_element = self.find_element(header_locator, 10)
        return header_element.text

