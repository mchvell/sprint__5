from framework.pageObject.NavBar import NavBarHelper
from framework.pageObject.ProfilePage import ProfilePageHelper


class TestLogOut:
    def test_logout(self, browser, authorization):
        nav_bar = NavBarHelper(browser)
        nav_bar.switcher("lk")

        profile_page = ProfilePageHelper(browser)

        profile_page.click_on_exit_button()
        url = browser.current_url
        assert "/login" in url
