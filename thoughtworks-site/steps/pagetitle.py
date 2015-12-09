import selenium
from selenium import webdriver

@given('we have Selenium installed')
def step_impl(context):
    assert selenium

@when('we open the TW web page')
def step_impl(context):
    driver = webdriver.Firefox()
    driver.get("http://www.thoughtworks.com/")
    context.title = driver.title
    driver.close()

@then('we check if the title is the expected')
def step_impl(context):
    assert "Agile Development and Experience Design | ThoughtWorks" in context.title
