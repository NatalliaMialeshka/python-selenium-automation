from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep

BEST_SELLERS_LINKS = (By.CSS_SELECTOR, "div._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq div[class*=_p13n-zg-nav-tab-all_style_zg-tabs-li]")


@then('Verify page has {expected_amount} links on the top')
def verify_page_top_link_count(context, expected_amount):
    expected_amount = int(expected_amount)
    best_sellers_links = context.driver.find_elements(*BEST_SELLERS_LINKS)
    assert len(best_sellers_links) == expected_amount, f'Expected {expected_amount} links, but got {len(best_sellers_links)}'