from appium.webdriver.webdriver import WebDriver
import pytest


class MobileDriverHandle:

    def get_driver(self):

        driver: 'WebDriver' = pytest.driver
        return driver

    def get_url(self, pstr_url):
        '''
        Open URL
        :param pstr_url: URL
        :return:
        '''
        try:
            self.get_driver().get(pstr_url)
        except Exception as e:
            raise Exception("Error occurred while opening the url " + pstr_url + "-->", e)

    def send_keys(self, locator, pstr_text_to_send):
        '''
        Send keys to element
        :param locator: locator of element
        :param pstr_text_to_send: text to send to element
        :return:
        '''
        try:
            self.wait_for_element_to_display(locator)
            self.get_element(locator).send_keys(pstr_text_to_send)
        except Exception as e:
            raise Exception("Exception occurred while sending text to element :", locator, "-->", e)

    def get_by(self, locator_type):
        try:
            if locator_type.lower() == 'xpath':
                locator_by = mobily_by.XPATH
            elif locator_type.lower() == 'id':
                locator_by = mobily_by.ID
            elif locator_type.lower() == 'css':
                locator_by = mobily_by.CSS_SELECTOR
            elif locator_type.lower() == 'link':
                locator_by = mobily_by.LINK_TEXT
            else:
                raise Exception("By of Locator not found for -->", locator_type)
            return locator_by
        except Exception as e:
            raise Exception("Error occurred while getting the by -->", e)