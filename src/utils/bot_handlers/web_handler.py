import calendar
import os
import time

import pytest

from src.utils.logger import logger
from src.utils.path_handler import PathHandler
from src.utils.config_handler import ConfigHandler

screen_shot_folder = PathHandler().get_screenshot_folder()
wait_time = ConfigHandler().get_waits()


class WebHandler:
    """

    """

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
    def get_page_url(self):
        return pytest.web_bot.get_url()

    def click(self, pstr_locator, pint_wait_for_display=wait_time.get('element_visible'), pbool_ignore_exception=False, pbool_ignore_screenshots=False):
        try:
            pytest.web_bot.click_element(pstr_locator, pint_wait_for_display)
        except Exception as e:
            error_message = f"Error occurred while Clicking the element {pstr_locator} {e}"
            logger.error(error_message)
            if pbool_ignore_exception is not True:
                raise
            else:
                return None
        finally:
            if not pbool_ignore_screenshots:
                self.take_screenshot()

    def type_text(self, pstr_locator,pstr_text, pint_wait_for_display=wait_time.get('element_visible'), pbool_ignore_screenshots=False):
        try:
            pytest.web_bot.type_text(pstr_locator, pint_wait_for_display,pstr_text)
        except Exception as e:
            error_message = f"Error occurred while Clicking the element {pstr_locator} {e}"
            logger.error(error_message)
            raise
        finally:
            if not pbool_ignore_screenshots:
                self.take_screenshot()


