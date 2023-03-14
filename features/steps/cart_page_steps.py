from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep
from selenium.webdriver.common.by import By


PRODUCT_NAME = (By.CSS_SELECTOR, "#sc-active-cart li")
#CART_COUNT = (By.ID, 'nav-cart-count')


@when('Open cart page')
def open_cart_page(context):
    context.app.cart_page.open_cart_page()
    #context.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')


@then('Verify that text "Your Amazon cart is empty" is shown')
def verify_search_result(context):
    context.app.cart_page.verify_cart_empty()
    #expected_result = 'Your Amazon Cart is empty'
    #actual_result = context.driver.find_element(By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty').text
    #assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'



@then('Verify cart has {expected_count} item(s)')
def verify_cart_count(context, expected_count):
    context.app.cart_page.verify_cart_has_one_item(expected_count)
    #actual_text = context.driver.find_element(*CART_COUNT).text
    #assert expected_count == actual_text, f'Expected {expected_count}, but got {actual_text}'