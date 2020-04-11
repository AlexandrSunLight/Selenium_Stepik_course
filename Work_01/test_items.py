import time
link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_AddToCartbutton(browser):
    browser.get(link)
    time.sleep(10)
    button = browser.find_element_by_css_selector("#add_to_basket_form > button")
    assert len(button.text) > 0, "Button not found"