from .base_page import BasePage

class Test_class:
    def test(self, browser):
        link = "https://demoqa.com/"
        page = BasePage(browser, link)
        page.open()
        page.should_be_current_url()
        page.go_to_elements()
        page.should_be_elements_page()
        page.go_to_check_box()
        page.should_be_checkbox_page()
        page.open_home_directory()
        page.should_be_downloads()
        page.open_downloads_directory()
        page.should_be_word_file()
        page.click_check_box_file()
        page.check_message()



