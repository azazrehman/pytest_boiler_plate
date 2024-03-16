from selenium import webdriver

class BotSelenium:

    driver = None
    browser_name = None
    driver_path = None

    def __init__(self, browser_on_tests_execute="chrome", driver_path=None):
        self.browser_name= browser_on_tests_execute
        self.driver_path= driver_path

    def open_url(self, url_to_open):
        self.driver.get(url=url_to_open)

    def launch_browser(self):
        if self.browser_on_tests_execute.lower() == 'chrome':
            if self.driver_path != None:
                self.driver = webdriver.Chrome(driver_path=self.driver_path)
            else:
                self.driver = webdriver.Chrome()
        elif self.browser_on_tests_execute.lower() == 'firefox':
            self.driver = webdriver.Firefox()
    
    def quit_browser(self):
        self.driver.quit()
