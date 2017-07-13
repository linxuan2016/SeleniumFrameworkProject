from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

user_info = {"linxuan": "flxyjrpa",
             "lisa": "flxyjrpa"}



@Given(u'I navigate to the login page')
def step_impl(context):
    context.browser.get("http://127.0.0.1:8000")


@When(u'I login with user "{username}"')
def step_impl(context, username):
    login_form_username = context.browser.find_element(By.XPATH,"//input[@type='text']")
    login_form_username.send_keys(username)
    login_from_password = context.browser.find_element(By.XPATH, "//input[@type='password']")
    login_from_password.send_keys(user_info[username])


@step('I click on the submit button')
def step_impl(context):
    button_submit = context.browser.find_element(By.XPATH, "//button[@type='submit']")
    button_submit.click()


@step('I am directed to the scrumboard page')
def step_impl(context):
    WebDriverWait(context.browser,10).until(
        EC.presence_of_element_located((By.XPATH, "//div/h3[text()='TO DO']"))
    )
    assert "TO DO" in context.browser.page_source


