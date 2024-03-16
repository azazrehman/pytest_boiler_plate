import pytest
from src.utils.logger import logger

class WebHandler:

    def open_url_in_browser(self, pstr_url):
        '''
        Open URL
        :param pstr_url: URL
        :return:
        '''
        try:
            pytest.web_bot.open_url(url_to_open=pstr_url)
        except Exception as e:
            error_message = f"Error occurred while opening the url {pstr_url} --> {e}"
            logger.error(error_message)
            raise Exception(error_message)
        