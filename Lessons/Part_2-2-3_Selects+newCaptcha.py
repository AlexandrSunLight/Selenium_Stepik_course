from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math
  
link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    x = int(x_element.text)
    y_element = browser.find_element_by_id("num2")
    y = int(y_element.text)
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(x + y))
    submit = browser.find_element_by_css_selector('[type="submit"]')
    submit.click()

finally:
    time.sleep(5)
    browser.quit()
    