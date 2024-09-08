from framework.pageObject.BasePage import BasePage
from framework.locators.NavBar import NavBarLocators


class NavBarHelper(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.nav_bar_tabs = NavBarLocators.NAVBAR_TABS

    # Исправлено после код ревью
    def switcher(self, nav_tab):
        nav_bar_locator = self.nav_bar_tabs.get(nav_tab)
        return self.find_element(nav_bar_locator, 15).click()

