from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page
from selenium.webdriver.common.by import By


class ProductPage(Page):

    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
    NEW_ARRIVALS = (By.CSS_SELECTOR, '#nav-subnav a[aria-label="New Arrivals"]')
    WOMEN_CAT = (By.CSS_SELECTOR, 'div.nav-template.nav-flyout-content div.mm-column a.mm-merch-panel[href*="fashion-womens"]')

    def click_add_to_cart(self):
        self.click(*self.ADD_TO_CART_BTN)

    def verify_product_added_to_cart(self):
        self.verify_url_contains_query('https://www.amazon.com/cart/smart-wagon')

    def hover_new_arrivals(self):
        new_arrivals_tab = self.find_element(*self.NEW_ARRIVALS)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals_tab)
        actions.perform()

    def verify_women_category(self):
        self.wait_for_element_appear(*self.WOMEN_CAT)




