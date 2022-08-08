from .base_page import BasePage
from pages.main_page import MainPage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        aassert "\login" in driver.current_url  
        assert True

    def should_be_login_form(self): 
        assert self.is_element_present(*LoginPageLocators.login_form), "Login link is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.register_form), "Login link is not presented"
        assert True