from pages.base_page import Page
from selenium.webdriver.common.by import By


class CartPage(Page):

    EMPTY_CART_TEXT = (By.XPATH, "//h2[contains(text(), 'Your Amazon Cart')]")
    CART_COUNT = (By.ID, 'nav-cart-count')

    def open_cart_page(self):
        self.open_url('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')


    def verify_cart_empty(self):
        self.verify_text('Your Amazon Cart is empty', *self.EMPTY_CART_TEXT)

    def verify_cart_has_one_item(self, text):
        self.verify_text(text, *self.CART_COUNT)