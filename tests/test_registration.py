from framework.pageObject.RegPage import RegPageHelper
from data.data_generator import TestDataGenerator


class TestRegistration:
    def test_registration_form_name(self, browser):
        reg_page = RegPageHelper(browser)
        reg_page.go_to_site()

        test_name = TestDataGenerator().generate_random_name()

        reg_page.fill_reg_form(name=test_name)
        name_input = reg_page.get_input_value("name")

        assert name_input == test_name

    def test_registration_form_email(self, browser):
        reg_page = RegPageHelper(browser)
        reg_page.go_to_site()

        test_email = TestDataGenerator().generate_random_email()

        reg_page.fill_reg_form(email=test_email)
        email_input = reg_page.get_input_value("email")

        assert "@" in email_input and "." in email_input

    def test_registration_form_password_length(self, browser):
        reg_page = RegPageHelper(browser)
        reg_page.go_to_site()

        test_password = TestDataGenerator().generate_random_password(length=6)

        reg_page.fill_reg_form(password=test_password)
        length_password = len(reg_page.get_input_value("password"))
        assert length_password >= 6

    def test_registration_form_incorrect_pass(self, browser):
        reg_page = RegPageHelper(browser)
        reg_page.go_to_site()

        test_password = TestDataGenerator().generate_random_password(length=2)

        reg_page.fill_reg_form(password=test_password)
        reg_page.click_on_input("name")
        incorrect_password = reg_page.get_incorrect_password_text()
        assert incorrect_password == "Некорректный пароль"
