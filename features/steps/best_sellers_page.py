from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep

BEST_SELLERS_LINKS = (By.CSS_SELECTOR, "div._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq div[class*=_p13n-zg-nav-tab-all_style_zg-tabs-li]")
TOP_LINKS = (By.CSS_SELECTOR, '#zg_header a')
HEADER = (By.CSS_SELECTOR, '#zg_banner_text')


@then('Verify page has {expected_amount} links on the top')
def verify_page_top_link_count(context, expected_amount):
    expected_amount = int(expected_amount)
    best_sellers_links = context.driver.find_elements(*BEST_SELLERS_LINKS)
    assert len(best_sellers_links) == expected_amount, f'Expected {expected_amount} links, but got {len(best_sellers_links)}'


@then('User can click through links and verify them')
def click_through_top(context):
    top_links = context.driver.find_elements(*TOP_LINKS)

    for i in range(len(top_links)):
        link_to_click = context.driver.find_elements(*TOP_LINKS)[i]
        link_text = link_to_click.text
        link_to_click.click()
        header_text = context.driver.find_element(*HEADER).text
        assert link_text in header_text, f'Expected{link_text} to be in {header_text}'