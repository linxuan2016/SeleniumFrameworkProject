from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://127.0.0.1:8000/")
login_form_username = driver.find_element_by_xpath("//input[@type='text']")
login_form_username.send_keys("linxuan")
login_form_password = driver.find_element_by_xpath("//input[@type='pasword']")
login_form_password.send_keys("flxyjrpa")
button_submit = driver.find_element_by_xpath("//button[@type='submit']")
button_submit.click()
assert "Scrumboard" in driver.title
