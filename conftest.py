import os,sys
sys.path.append(os.getcwd())

import pytest
from src.utils.bot_handlers.bots.bot_playwright import BotPlaywright
from src.utils.bot_handlers.bots.bot_selenium import BotSelenium



def common_config():
    print('Conftest Comon config')
    pytest.web_bot = None
    pytest.mobile_bot = None

@pytest.fixture(scope='session', autouse=True)
def before_all():
    print(f'Before All :)')
        # TODO - Update it to use from config
    frame_work = 'playwright' 
    browser = 'chrome'
    if frame_work == 'selenium':
        print('Inside selenium - Before')
        pytest.web_bot = BotSelenium(browser_on_tests_execute=browser)
    elif frame_work == 'playwright':
        pytest.web_bot = BotPlaywright(browser_on_tests_execute=browser)

def setup_method(self, method):
    print(f'Setup Method :)')
        # TODO - Update it to use from config
    frame_work = 'selenium' 
    browser = 'chrome'
    if frame_work == 'selenium':
            print('Inside selenium - Setup mothod')
            pytest.web_bot = BotSelenium(browser_on_tests_execute=browser)
    elif frame_work == 'playwright':
            pytest.web_bot = BotPlaywright(browser_on_tests_execute=browser)

def teardown_method(self, method):
        print(f'TearDown Method :)')

