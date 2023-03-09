from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

PRIVACY_NOTICE = (By.CSS_SELECTOR, "a[href='https://www.amazon.com/privacy']")

@given('Open Amazon T&C page')
def amazon_tc_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Click on Amazon Privacy Notice link')
def click_img(context):
    context.driver.find_element(*PRIVACY_NOTICE).click()


@then('Verify Amazon Privacy Notice page is opened')
def verify_blog_page_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/'))



