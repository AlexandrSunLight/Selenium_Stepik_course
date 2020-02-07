from selenium import webdriver
import time
import math
import os 
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()
    """time.sleep(3)
    alert = browser.switch_to.alert
    alert.accept()
    """
    time.sleep(1)
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    input = browser.find_element_by_id("answer")
    input.send_keys(y)
    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()

finally:
    time.sleep(5)
    browser.quit()
    