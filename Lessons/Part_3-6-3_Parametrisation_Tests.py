import pytest
from selenium import webdriver
import time
import math

def answer():
  return math.log(int(time.time()))
  
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    
class TestAnswers(object):
    @pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1" ])
    def test_should_be_correct_answer(self, browser, links):
        link = F'{links}'
        browser.get(link)
        time.sleep(5)
        textbox = browser.find_element_by_css_selector("textarea.textarea")
        textbox.send_keys(str(answer()))
        button = browser.find_element_by_class_name('submit-submission')
        button.click()
        time.sleep(3)
        hint = browser.find_element_by_class_name('smart-hints__hint').text
        assert "Correct!" == hint
        