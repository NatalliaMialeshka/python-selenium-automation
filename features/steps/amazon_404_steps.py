from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

DOG_IMAGE = (By.ID, 'd' )


@given ('Store original window')
def store_current_window(context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)


@when('Click on a dog image')
def click_img(context):
    context.driver.find_element(*DOG_IMAGE).click()


@when('Switch to new window')
def switch_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    windows = context.driver.window_handles
    context.driver.switch_to.window(windows[1])


@then('Verify blog is opened')
def verify_blog_page_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.aboutamazon.com/news/'))


@then('Close page')
def close_window(context):
    context.driver.close()


@then('Return to original window')
def return_to_original_page(context):
    context.driver.switch_to.window(context.original_window)


