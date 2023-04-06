from pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResultsPage(Page):

    SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
    SUBNAV = (By.CSS_SELECTOR, '#nav-subnav[data-category="{CATEGORY}"]')

    def get_subnav_locator(self,category):
        return[self.SUBNAV[0], self.SUBNAV[1].replace("{CATEGORY}", category)]

    def verify_search_result(self, expected_text):
       actual_result = self.driver.find_element(*self.SEARCH_RESULT).text
       assert expected_text == actual_result, f'Expected {expected_text} but got actual {actual_result}'

    def click_first_product(self):
        self.click(*self.PRODUCT_PRICE)

    def verify_selected_dept(self,category):
        locator = self.get_subnav_locator(category)
        self.wait_for_element_appear(*locator)



