from playwright.sync_api import sync_playwright
from src.utils.logger import logger


class BotPlaywright:
    browser_name = None
    page = None
    browser = None
    my_bot = None

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

                if self.my_bot is None:
                    self.my_bot = sync_playwright().start()
                if self.browser_name.lower() == 'chromium' or self.browser_name.lower() == 'chrome':
                    self.browser = self.my_bot.chromium.launch(**options)
                elif self.browser_name.lower() == 'firefox':
                    self.browser = self.my_bot.firefox.launch(**options)
                self.page = self.browser.new_page()
        except Exception as e:
            logger.error(
                f"Error while Launching browser {e}")
            raise

    def quit_browser(self):
        self.browser.close()
        self.page = None
        self.browser = None

    def get_url(self):
        return self.page.url

    def take_and_save_screenshot(self, directory_path):
        self.page.screenshot(path=directory_path, full_page=True)

    def wait_for_locator(self, locator, waiting_time, waiting_state="visible"):
        waiting_time_milliseconds = waiting_time*1000
        self.page.locator(locator).wait_for(timeout=waiting_time_milliseconds, state=waiting_state)

    def click_element(self, pstr_locator, pint_waiting_time):
        self.wait_for_locator(pstr_locator, pint_waiting_time)
        self.page.locator(pstr_locator).click()

    def popup_handler(self, accept=True):
        if accept:
            self.page.on("dialog", lambda dialog: dialog.accept())
        else:
            self.page.on("dialog", lambda dialog: dialog.dismiss())

    def type_text(self, pstr_locator, pint_waiting_time, pstr_text):
        self.wait_for_locator(pstr_locator, pint_waiting_time)
        self.page.locator(pstr_locator).type(pstr_text)
