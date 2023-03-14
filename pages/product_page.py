from pages.base_page import Page
from selenium.webdriver.common.by import By


class ProductPage(Page):

    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')

    def click_add_to_cart(self):
        self.click(*self.ADD_TO_CART_BTN)

    def verify_product_added_to_cart(self):
        self.verify_url_contains_query('https://www.amazon.com/cart/smart-wagon')


