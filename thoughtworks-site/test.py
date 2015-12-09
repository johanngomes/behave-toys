import logging
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.thoughtworks.com")
print(driver.title)
driver.close()
