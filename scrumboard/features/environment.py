
from selenium import webdriver

def before_all(context):
    context.browser = webdriver.Firefox()
    # context.browser = webdriver.Chrome() if you have set chromedriver in your PATH
    #context.browser.set_page_load_timeout(20)
    context.browser.implicitly_wait(10)
    context.browser.maximize_window()
    #context.browser.get("http://127.0.0.1:8000")

def after_all(context):
    context.browser.quit()

