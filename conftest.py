import pytest
from selenium import webdriver

from playwright.sync_api import sync_playwright

class Base:

    def common_config(self):
        pytest.web_bot = None
        pytest.mobile_bot = None

    #@pytest.fixture(scope='session', autouse=True)
    def before_all(self):
        print(f'Before All :)')

    def setup_method(self, method):
        print(f'Setup Method :)')
         # TODO - Update it to use from config
        frame_work = 'selenium' 
        browser = 'chrome'
        if frame_work is 'selenium':
             self.run_with_selenium(browser)
        elif frame_work is 'playwright':
             self.run_with_playwright('chromium')

    def teardown_method(self, method):
         print(f'TearDown Method :)')

    def run_with_selenium(browser):
        if browser is 'chrome':
                pytest.web_bot = webdriver.Chrome()
    def run_with_playwright(browser):
        with sync_playwright() as playwright:
            browser = playwright.browser.launch()
