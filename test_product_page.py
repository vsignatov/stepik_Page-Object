from pages.base_page import BasePage
from pages.locators import page_elements
from pages.locators import basket_elements
import pytest        
import time

@pytest.mark.parametrize('promo_page', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
                                  
class TestUserAddToBasketFromProductPage ():
    def test_guest_cant_see_success_message (browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = BasePage (browser, link)
        page.open_browser()
        check = page.is_not_element_present(page_elements.alert_successfull)
        assert check == True
    
    def test_guest_can_add_product_to_basket(browser, promo_page):
        link = f"{promo_page}"
        page = BasePage (browser, link)
        page.open_browser()
        book_name = browser.find_element(*page_elements.BookName).text
        book_price = browser.find_element(*page_elements.BookPrice).text
        button = browser.find_element(*page_elements.Button)
        button.click()
        page.solve_quiz_and_get_code()
        message_book_name = browser.find_element(*page_elements.alert_successfull).text
        assert book_name == message_book_name, "???????????????????????? ???????????? ??????????????????"
        button_basket = browser.find_element (*basket_elements.ButtonBasket)
        button_basket.click ()
        book_price_basket = browser.find_element (*basket_elements.Book_price_in_basket).text
        assert book_price == book_price_basket, "???????? ?? ?????????????? ????????????????????"
    
    
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = BasePage (browser, link)
    page.open_browser()
    button = browser.find_element(*page_elements.Button)
    button.click()
    page.solve_quiz_and_get_code()
    check = page.is_not_element_present(page_elements.alert_successfull)
    assert check == True
   

   
def test_message_disappeared_after_adding_product_to_basket (browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = BasePage (browser, link)
    page.open_browser()
    button = browser.find_element(*page_elements.Button)
    button.click()
    page.solve_quiz_and_get_code()
    check = page.is_disappeared(page_elements.alert_successfull)
    assert check == True