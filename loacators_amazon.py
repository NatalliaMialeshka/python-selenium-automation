from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service("/Users/belar/Automation/python-selenium-automation/chromedriver.exe")
driver = webdriver.Chrome(service=service)

#HW Part 2
driver.find_element(By.XPATH, "//*[@aria-label='Amazon']")

driver.find_element(By.ID, "ap_email")
driver.find_element(By.ID, "continue")

driver.find_element(By.XPATH, "//span[@class='a-expander-prompt' and contains(text(), 'Need help?')]")

driver.find_element(By.ID, "auth-fpp-link-bottom")
driver.find_element(By.ID, "ap-other-signin-issues-link")

driver.find_element(By.ID, "createAccountSubmit")

driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[text()='Conditions of Use']")
driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[text()='Privacy Notice']")

#HW Part 3
driver.get('https://www.amazon.com/')

driver.find_element(By.XPATH, "//span[@class='nav-line-2' and text()='& Orders']").click()

expected_result = 'Sign in'
actual_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small' and contains(text(), 'Sign in')]").text
print(actual_result)

expected_result2 = 'Email or mobile phone number'
actual_result2 = driver.find_element(By.XPATH, "//label[@class='a-form-label' and contains(text(), 'Email or mobile phone number')]").text
print(actual_result2)

assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'
assert expected_result2 == actual_result2, f'Expected {expected_result2} but got actual {actual_result2}'
print('Test cases passed')

driver.quit()