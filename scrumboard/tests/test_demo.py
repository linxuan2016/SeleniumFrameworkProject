from django.test import TestCase

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DemoTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r'c:\Utilities\geckodriver.exe')
        self.driver.implicitly_wait(3)
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.maximize_window()

    def test_search(self):
        login_form_username = self.driver.find_element_by_xpath("//input[@type='text']")
        login_form_username.send_keys("linxuan")

        # try:
        #     login_from_password = WebDriverWait(self.driver, 10).until(
        #         EC.presence_of_element_located((By.XPATH, "//input[@type='password'"))
        #     )
        # finally:
        #     self.driver.quit()

        login_from_password = self.driver.find_element_by_xpath("//input[@type='password']")
        login_from_password.send_keys("flxyjrpa")
        button_submit = self.driver.find_element_by_xpath("//button[@type='submit']")
        button_submit.click()
        assert "Scrumboard" in self.driver.title

    def tearDown(self):
        self.driver.close()

