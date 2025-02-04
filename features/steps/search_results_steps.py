from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep

SEARCH_RESULTS = (By.CSS_SELECTOR, "div[cel_widget_id*='MAIN-SEARCH_RESULTS-']")
PRODUCT_IMAGE = (By.CSS_SELECTOR, "div[cel_widget_id*='MAIN-SEARCH_RESULTS-'] div.s-product-image-container")
PRODUCT_NAME_FIELD = (By.CSS_SELECTOR, "div[cel_widget_id*='MAIN-SEARCH_RESULTS-'] a.a-link-normal[href*='/gp/slredirect/']")

@when('Click on the first product')
def click_first_product(context):
    context.app.search_results_page.click_first_product()
    context.driver.implicitly_wait(2)


@then('Verify that text {expected_result} is shown')
def verify_search_result(context, expected_result):
    context.app.search_results_page.verify_search_result(expected_result)
    #actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    #assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'


@then('Verify that every product has name and image')
def verify_every_prod_has_name_and_image(context):
    all_products = context.driver.find_elements(*SEARCH_RESULTS)
    print('All results: ', all_products)

    for item in all_products:
        context.driver.find_element(*PRODUCT_IMAGE).is_displayed()
        context.driver.find_element(*PRODUCT_NAME_FIELD).is_displayed()


@then('Verify {category} department is selected')
def verify_selected_dept(context, category):
    context.app.search_results_page.verify_selected_dept(category)