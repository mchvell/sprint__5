from framework.pageObject.MainPage import MainPageHelper
from framework.pageObject.AuthPage import AuthPageHelper
from framework.pageObject.NavBar import NavBarHelper
from framework.pageObject.RegPage import RegPageHelper
from data.auth_data import AuthData as user


class TestAuth:
    def test_auth_from_constructor_page(self, browser):
        main_page = MainPageHelper(browser)
        main_page.go_to_site()
        main_page.click_on_enter_button()

        auth_page = AuthPageHelper(browser)
        auth_page.fill_auth_form(email=user.email, password=user.password)
        auth_page.click_enter_button()

        nav_bar = NavBarHelper(browser)
        nav_bar.switcher("lk")
        assert "/account/profile" in browser.current_url

    def test_auth_from_auth_page(self, browser):
        auth_page = AuthPageHelper(browser)
        auth_page.go_to_site()
        auth_page.fill_auth_form(email=user.email, password=user.password)
        auth_page.click_enter_button()

        nav_bar = NavBarHelper(browser)
        nav_bar.switcher("lk")
        assert "/account/profile" in browser.current_url

    # Правки после код ревью: упростил последний тест и удалил тест с авторизацией через навбар, тк
    # уже тестируем функциональность навбара в рамках test_nav_bar
    def test_auth_from_reg_page(self, browser):
        reg_page = RegPageHelper(browser)
        reg_page.go_to_site()
        reg_page.click_on_auth_link()

        auth_page = AuthPageHelper(browser)
        auth_page.fill_auth_form(email=user.email, password=user.password)
        auth_page.click_enter_button()

        nav_bar = NavBarHelper(browser)
        nav_bar.switcher("lk")
        assert "/account/profile" in browser.current_url
