import pytest
from selenium import webdriver
from framework.pageObject.AuthPage import AuthPageHelper
from data.auth_data import AuthData as user


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def authorization(browser):
    auth_page = AuthPageHelper(browser)
    auth_page.go_to_site()
    auth_page.fill_auth_form(
        email=user.email,
        password=user.password
    )
    auth_page.click_enter_button()
