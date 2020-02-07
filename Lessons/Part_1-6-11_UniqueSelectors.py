from selenium import webdriver
import time 

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector("div.first_block> div .first")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("div.first_block> div .second")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("div.first_block> div .third")
    input3.send_keys("e-mail")
    input4 = browser.find_element_by_css_selector("div.second_block> div .first")
    input4.send_keys("Xiaomi")
    input5 = browser.find_element_by_css_selector("div.second_block> div .second")
    input5.send_keys("Russia")
    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()

finally:
    time.sleep(30)
    browser.quit()