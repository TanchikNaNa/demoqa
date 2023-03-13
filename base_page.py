from .locators import BasePageLocators
from selenium.common.exceptions import NoSuchElementException

class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def go_to_elements(self):
        elments_button= self.browser.find_element(*BasePageLocators.ELEMENTS)
        elments_button.click()

    def go_to_check_box(self):
     check_box_button = self.browser.find_element(*BasePageLocators.check_box)
     check_box_button.click()

    def open_home_directory(self):
     open_button = self.browser.find_element(*BasePageLocators.open_home)
     open_button.click()

    def open_downloads_directory(self):
     open_button= self.browser.find_element(*BasePageLocators.open_downloads)
     open_button.click()

    def click_check_box_file(self):
     check_box = self.browser.find_element(*BasePageLocators.check_box_file)
     check_box.click()

    def should_be_current_url(self):
        current_url = self.browser.current_url
        assert "demoqa" in current_url, "incorrect url"

    def should_be_elements_page(self):
        current_url = self.browser.current_url
        assert "elements" in current_url, "incorrect url"       

    def should_be_checkbox_page(self):
        current_url = self.browser.current_url
        assert "checkbox" in current_url, "incorrect url" 

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True   
    
    def should_be_downloads(self):
        assert self.is_element_present(*BasePageLocators.open_downloads), "Directory HOME isn't open"

    def should_be_word_file(self):
        assert self.is_element_present(*BasePageLocators.check_box_file), "Directory DOWNLOADS isn't open"

    def check_message(self):
       message1 = self.browser.find_element(*BasePageLocators.text1)
       message2 = self.browser.find_element(*BasePageLocators.text2)
       message3 = message1.text + message2.text
       assert "You have selected :wordFile" in message3
         
