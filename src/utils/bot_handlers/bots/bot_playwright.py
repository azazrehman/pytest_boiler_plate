
from playwright.sync_api import sync_playwright

class BotPlaywright:
    def __init__(self, browser_on_tests_execute):
        with sync_playwright() as my_bot:
            if browser_on_tests_execute.lower() == 'chromium' or browser_on_tests_execute.lower() == 'chrome':
                self.browser = my_bot.chromium.launch() 
            elif browser_on_tests_execute.lower() == 'firefox':
                self.browser = my_bot.firefox.launch() 
            self.page = self.browser.new_page()

    def open_url(self, url_to_open):
        self.page.goto(url=url_to_open, wait_until='networkidle')