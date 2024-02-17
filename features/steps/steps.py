from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.common.exceptions import NoSuchElementException
from time import sleep

@given('Google Chrome is open and the user has navigated to the Target webpage')
def open_target(context):
    context.driver.get('https://www.target.com/')

@when('the user clicks on the cart icon without having put any items into it')
def click_on_the_cart_icon(context):
    context.driver.find_element(By.ID, '//*[@id="headerPrimary"]/a[5]').click()

xpath = '//*[@id="headerPrimary"]/a[5]'

@then('the "Your cart is empty" message appears')
def check_exists_by_xpath(context):
    try:
        context.driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True

