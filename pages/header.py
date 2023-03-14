from pages.base_page import Page
from selenium.webdriver.common.by import By

class Header(Page):
    AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    ORDERS_BUTTON = (By.XPATH, "//span[@class='nav-line-2' and text()='& Orders']")
    CART = (By.ID, "nav-cart")

    def input_search_text(self, text):
        self.input_text(text, *self.AMAZON_SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def click_orders(self):
        self.click(*self.ORDERS_BUTTON)

    def click_cart(self):
        self.click(*self.CART)

