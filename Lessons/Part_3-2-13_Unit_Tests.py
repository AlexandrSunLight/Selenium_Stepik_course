from selenium import webdriver
import time, unittest

class TestRegistratuon(unittest.TestCase):
    def test_Registration_1(self):
        link = "http://suninjuly.github.io/registration1.html"
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
        time.sleep(3)
        response = browser.find_element_by_tag_name("h1").text
        self.assertIn("Congratulations!", response, "Should be 'Congratulations!' string")
        
    def test_Registration_2(self):
        link = "http://suninjuly.github.io/registration2.html"
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
        time.sleep(3)
        response = browser.find_element_by_tag_name("h1").text
        self.assertIn("Congratulations!", response, "Should be 'Congratulations!' string")
        
if __name__ == "__main__":
    unittest.main()