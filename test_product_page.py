from pages.base_page import BasePage
from pages.locators import page_elements
from pages.locators import basket_elements
import pytest        

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
                                                                            
def test_AddItemToBasket(browser, promo_page):
    link = f"{promo_page}"
    page = BasePage (browser, link)
    page.open_browser()
    book_name = browser.find_element(*page_elements.BookName).text
    book_price = browser.find_element(*page_elements.BookPrice).text
    button = browser.find_element(*page_elements.Button)
    button.click()
    alert = BasePage(browser, link)
    alert.solve_quiz_and_get_code()
    message_book_name = browser.find_element(*page_elements.MessageBookName).text
    assert book_name == message_book_name, "Наименование товара отличаеся"
    button_basket = browser.find_element (*basket_elements.ButtonBasket)
    button_basket.click ()
    book_price_basket = browser.find_element (*basket_elements.Book_price_in_basket).text
    assert book_price == book_price_basket, "Цена в корзине отличается"
    