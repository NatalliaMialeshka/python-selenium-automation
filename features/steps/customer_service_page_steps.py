from selenium.webdriver.common.by import By
from behave import when, then


MAIN_HEADER = (By.XPATH, "//h1[@class='fs-heading bolded' and text()='Welcome to Amazon Customer Service']")
CUSTOMER_SERVICE_LINKS = (By.CSS_SELECTOR, "div.issue-card-container div.issue-card-wrapper")
SECONDARY_HEADER = (By.XPATH, "//h2[@class='fs-heading bolded' and text()='Search our help library']")
SEARCH_BAR = (By.ID, "hubHelpSearchInput")
TOPIC_TITLE = (By.XPATH, "//h2[@class='fs-heading bolded' and text()='All help topics']")
HELP_LINKS = (By.CSS_SELECTOR, "ul.help-topics li.help-topics")


@then('Verify main header presents')
def verify_header_presented(context):
    context.driver.find_element(*MAIN_HEADER)


@then('Verify {expected_amount} links are presented on the page')
def verify_customer_service_links_count(context, expected_amount):
    expected_amount = int(expected_amount)
    customer_service_links = context.driver.find_elements(*CUSTOMER_SERVICE_LINKS)
    assert len(customer_service_links) == expected_amount, f'Expected {expected_amount} links, but got {len(customer_service_links)}'


@then('Verify secondary header presented')
def verify_secondary_header_presented(context):
    context.driver.find_element(*SECONDARY_HEADER)


@then('Verify search bar is presented')
def verify_search_bar_presented(context):
    context.driver.find_element(*SEARCH_BAR)


@then('Verify the topic title is presented')
def verify_topic_title_presented(context):
    context.driver.find_element(*TOPIC_TITLE)


@then('Verify there are {expected_amount} help links')
def verify_page_links_amount(context, expected_amount):
    expected_amount = int(expected_amount)
    help_links = context.driver.find_elements(*HELP_LINKS)
    assert len(help_links) == expected_amount, f'Expected {expected_amount} links, but got {len(help_links)}'