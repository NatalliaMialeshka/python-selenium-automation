from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service("/Users/belar/Automation/python-selenium-automation/chromedriver.exe")
driver = webdriver.Chrome(service=service)

#HW part 1
driver.find_element(By.CSS_SELECTOR, 'a.a-link-nav-icon')
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

driver.find_element(By.ID, 'ap_customer_name')
driver.find_element(By.ID, 'ap_email')
driver.find_element(By.ID, 'ap_password')

driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

driver.find_element(By.XPATH, "//div[@class='a-alert-content' and contains(text(), 'Passwords must be at least 6 characters.')]")

driver.find_element(By.ID, 'ap_password_check')
driver.find_element(By.ID, 'continue')

driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[text()='Conditions of Use']")
driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[text()='Privacy Notice']")

driver.find_element(By.XPATH, "//a[@class='a-link-emphasis' and contains(text(), 'Sign in')]")