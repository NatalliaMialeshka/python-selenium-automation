from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import when, given, then
from time import sleep


#ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")


@given('Open Amazon product {product_id} page')
def open_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')


@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.app.product_page.click_add_to_cart()
    context.app.product_page.verify_product_added_to_cart()
    #context.app.wait.until(EC.url_contains('https://www.amazon.com/cart/smart-wagon'))


@when('Hover over New Arrivals Tab')
def hover_new_arrivals(context):
    context.app.product_page.hover_new_arrivals()


@then('Verify user can click through colors')
def verify_user_can_select_colors(context):
    context.driver.find_element(*COLOR_OPTIONS).click()

    all_color_options = context.driver.find_elements(*COLOR_OPTIONS)
    print('All colors:', all_color_options)
    expected_colors =  ['A-armygreen', 'A-black', 'A-blue-01', 'A-blue01', 'A-burgundy']

    actual_colors = []
    for color in all_color_options[:5]:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        print('Current color: ', current_color)
        actual_colors += [current_color]

    assert expected_colors == actual_colors, f'Expected {expected_colors}, but got {actual_colors}'


@then('Verify user can select different colors')
def verify_user_can_pick_different_colors(context):
    all_color_options = context.driver.find_elements(*COLOR_OPTIONS)
    for color in all_color_options:
        color.click()


@then('Verify that user sees category Women')
def verify_women_category(context):
    context.app.product_page.verify_women_category()
