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
        
    def register_new_user (mail, password):
        open_browser()
        should_be_register_form()
        input_1 = (*.LoginPageLocators.register_email_input)
        input_1.send_keys (mail)
        input_2 = (*.LoginPageLocators.register_password_input)
        input_2.send_keys (password)
        input_3 = (*.LoginPageLocators.confirm_password_input)
        input_3.send_keys (password)
        
        