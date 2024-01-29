import pytest

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
            raise Exception("Error occurred while opening the url " + pstr_url + "-->", e)
        