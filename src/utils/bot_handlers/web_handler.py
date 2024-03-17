import calendar
import os
import time

import pytest

from src.utils.logger import logger
from src.utils.path_handler import PathHandler
from src.utils.config_handler import ConfigHandler
screen_shot_folder = PathHandler().get_screenshot_folder()
wait_time = ConfigHandler().ALL_WAITS

class WebHandler:

    def open_url_in_browser(self, pstr_url):
        '''
        Open URL
        :param pstr_url: URL
        :return:
        '''
        try:
            pytest.web_bot.open_url(url_to_open=pstr_url)
            self.take_screenshot()
        except Exception as e:
            error_message = f"Error occurred while opening the url {pstr_url} --> {e}"
            logger.error(error_message)
            raise Exception(error_message)

    def take_screenshot(self, pstr_file_name="screenshot"):
        file_name = f"{pstr_file_name}_{int(calendar.timegm(time.gmtime()))}"
        folder_path = f"{screen_shot_folder}/{pytest.current_test_name}"
        pytest.web_bot.take_and_save_screenshot(f"{folder_path}/{file_name}.png")

    def terminate_browser(self):
        pytest.web_bot.quit_browser()

    def click(self, locator, wait_for_display=):
        pytest.web_bot.click_element(locator, wait_for_display)