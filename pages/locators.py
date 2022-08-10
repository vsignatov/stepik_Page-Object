from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    login_form = (By.ID, "login_form")
    register_form = (By.ID, "register_form")
    
    
class product_page ():
    add_to_basket = (By.CSS_SELECTOR, ".btn_add_to_basket")
    
class page_elements():
    BookName = (By.CSS_SELECTOR, ".product_main h1")
    BookPrice = (By.CSS_SELECTOR, ".product_main .price_color") 
    Button = (By.CSS_SELECTOR, ".btn-add-to-basket")
    alert_successfull = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    
class basket_elements():
    ButtonBasket = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    Book_price_in_basket = (By.CSS_SELECTOR, "#basket_formset > div > div > div.col-sm-1 > p")