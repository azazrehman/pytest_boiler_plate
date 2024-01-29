from selenium import webdriver

class BotSelenium:

    driver = None

    def __init__(self, browser_on_tests_execute="chrome"):
        if browser_on_tests_execute.lower() == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser_on_tests_execute.lower() == 'firefox':
            self.driver = webdriver.Chrome()

    def open_url(self, url_to_open):
        self.driver.get(url=url_to_open)

    # TODO Add other wrapper methods for Selenium actions