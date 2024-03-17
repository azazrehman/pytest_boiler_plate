from playwright.sync_api import sync_playwright
from src.utils.logger import logger


class BotPlaywright:
    browser_name = None
    page = None
    browser = None

    def __init__(self, browser_on_tests_execute):
        self.browser_name = browser_on_tests_execute
        self.launch_browser()

    def open_url(self, url_to_open):
        self.page.goto(url=url_to_open, wait_until='networkidle')

    def launch_browser(self):
        try:
            if self.page is None:
                options = {
                    # Add your browser options here
                    "headless": False,  # Example option
                    "slow_mo": 1000  # Example option
                }
                # with sync_playwright() as my_bot:
                my_bot = sync_playwright().start()
                if self.browser_name.lower() == 'chromium' or self.browser_name.lower() == 'chrome':
                    self.browser = my_bot.chromium.launch(**options)
                elif self.browser_name.lower() == 'firefox':
                    self.browser = my_bot.firefox.launch(**options)
                self.page = self.browser.new_page()
        except Exception as e:
            logger.error(
                f"Error while Launching browser {e}")
            raise

    def quit_browser(self):
        self.browser.close()

    def take_and_save_screenshot(self, directory_path):
        self.page.screenshot(path=directory_path, full_page=True)
