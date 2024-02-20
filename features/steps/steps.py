from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Google Chrome is open and the user has navigated to the Target webpage')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('the user clicks on the cart icon without having put any items into it')
def click_on_the_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartIcon']").click()


@then('Your cart is empty message appears')
def verify_cart_is_empty(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    print(actual_text)
    expected_result = 'Your cart is empty'
    assert expected_result in actual_text, f'Expected result {expected_result} + not in {actual_text}'