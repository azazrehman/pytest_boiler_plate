from appium.webdriver.common.mobileby import MobileBy as mobily_by, MobileBy
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.webdriver import WebDriver
import time
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

    def get_by_from_identifier(self, pstr_element_locator):
        try:
            #print("INSIDE GET ELEMENT")
            ele = ""
            split_type = pstr_element_locator.split("||")
            #print(split_type)
            #print("PLATFORM NAME IS")
            #print(self.get_driver().capabilities["platformName"])
            if self.get_driver().capabilities["platformName"] == "Android":
                #print("INSIDE ANDROID GET ELEMENT")
                pstr_element_locator = split_type[0]
                #print(pstr_element_locator)
                split_locator = pstr_element_locator.split("=", 1)
                #print(split_locator)
                locator_type_by = self.get_by(split_locator[0])
                return locator_type_by
            if self.get_driver().capabilities["platformName"] == "iOS":
                pstr_element_locator = split_type[1]
                split_locator = pstr_element_locator.split("=", 1)
                locator_type_by = self.get_by(split_locator[0])
                return locator_type_by
            return ele
        except Exception as e:
            raise Exception("Error occurred while getting by from locator identifier :" + pstr_element_locator + "-->",
                            e)

    def get_element_locator_identifer(self, pstr_element_locator):
        try:
            #print("INSIDE GET ELEMENT")
            ele = ""
            split_type = pstr_element_locator.split("||")
            #print(split_type)
            #print("PLATFORM NAME IS")
            #print(self.get_driver().capabilities["platformName"])
            if self.get_driver().capabilities["platformName"] == "Android":
                #print("INSIDE ANDROID GET ELEMENT")
                pstr_element_locator = split_type[0]
                #print(pstr_element_locator)
                split_locator = pstr_element_locator.split("=", 1)
                #print(split_locator)
                locator_type_by = self.get_by(split_locator[0])
                #print(locator_type_by)
                locator_identifer = split_locator[1]
                return locator_identifer
            if self.get_driver().capabilities["platformName"] == "iOS":
                pstr_element_locator = split_type[1]
                split_locator = pstr_element_locator.split("=", 1)
                locator_type_by = self.get_by(split_locator[0])
                locator_identifer = split_locator[1]
                return locator_identifer
            return ele
        except Exception as e:
            raise Exception("Error occurred while getting the element :" + pstr_element_locator + "-->", e)

    def get_element(self, pstr_element_locator):
        try:
            #print("INSIDE GET ELEMENT")
            ele = ""
            split_type = pstr_element_locator.split("||")
            #print(split_type)
            #print("PLATFORM NAME IS")
            #print(self.get_driver().capabilities["platformName"])
            if self.get_driver().capabilities["platformName"] == "Android":
                #print("INSIDE ANDROID GET ELEMENT")
                pstr_element_locator = split_type[0]
                #print(pstr_element_locator)
                split_locator = pstr_element_locator.split("=", 1)
                #print(split_locator)
                locator_type_by = self.get_by(split_locator[0])
                #print(locator_type_by)
                locator_identifer = split_locator[1]
                ele = self.get_driver().find_element(by=locator_type_by, value=locator_identifer)
            if self.get_driver().capabilities["platformName"] == "iOS":
                pstr_element_locator = split_type[1]
                split_locator = pstr_element_locator.split("=", 1)
                locator_type_by = self.get_by(split_locator[0])
                locator_identifer = split_locator[1]
                ele = self.get_driver().find_element(by=locator_type_by, value=locator_identifer)
            return ele
        except Exception as e:
            raise Exception("Error occurred while getting the element :" + pstr_element_locator + "-->", e)

    def wait_for_element_to_display(self, pstr_locator, pint_time_to_wait=20):
        try:
            #print("INSIDE ELEMENT TO DISPLAY")
            count = 0
            EC.visibility_of_element_located(
                (self.get_by_from_identifier(pstr_locator), self.get_element_locator_identifer(pstr_locator)))
            while not self.get_element(pstr_locator).is_displayed():
                time.sleep(1)
                count += 1
                if count > pint_time_to_wait:
                    break

            WebDriverWait(self.get_driver(), pint_time_to_wait).until(EC.visibility_of(self.get_element(pstr_locator)))
        except Exception as e:
            raise Exception("Exception occurred while waiting for element to be located :", pstr_locator, " --> ", e)

    def wait_for_element_to_be_visible(self, pstr_locator, pint_time_to_wait=20):
        WebDriverWait(self.get_driver(), pint_time_to_wait).until(
            EC.visibility_of_element_located(
                (self.get_by(pstr_locator), self.get_element_locator_identifer(pstr_locator))))

    def wait_for_loading_icon_be_disappear(self, pstr_locator, pint_timeout=10):
        try:
            element1 = WebDriverWait(self.get_driver(), pint_timeout).until(EC.visibility_of_element_located(
                (self.get_by_from_identifier(pstr_locator), self.get_element_locator_identifer(pstr_locator))))
            print("waited for x sec")
            time.sleep(10)
            element2 = WebDriverWait(self.get_driver(), pint_timeout+pint_timeout).until(EC.visibility_of_element_located(
                (self.get_by_from_identifier(pstr_locator), self.get_element_locator_identifer(pstr_locator))))
            print("waited for x+x sec")
        except Exception as e:
            print(e)

    def wait_for_element_to_be_clickable(self, pstr_locator, pint_time_to_wait=5):
        try:
            WebDriverWait(self.get_driver(), pint_time_to_wait).until(
                EC.element_to_be_clickable(self.get_element(pstr_locator)))
        except Exception as e:
            raise Exception("Exception occurred while waiting for element to be located :", pstr_locator, " --> ", e)

    def click_element(self, pstr_locator, wait=20):
        try:
            self.wait_for_element_to_display(pstr_locator, wait)
            self.get_element(pstr_locator).click()
        except Exception as e:
            raise Exception("Exception occurred while clicking element :", pstr_locator, "-->", e)

    def get_elements(self, pstr_element_locator):
        try:
            self.wait_for_element_to_display(pstr_element_locator)
            # print("INSIDE GET ELEMENT")
            ele = ""
            split_type = pstr_element_locator.split("||")
            # print(split_type)
            # print("PLATFORM NAME IS")
            # print(self.get_driver().capabilities["platformName"])
            if self.get_driver().capabilities["platformName"] == "Android":
                # print("INSIDE ANDROID GET ELEMENT")
                pstr_element_locator = split_type[0]
                # print(pstr_element_locator)
                split_locator = pstr_element_locator.split("=", 1)
                # print(split_locator)
                locator_type_by = self.get_by(split_locator[0])
                # print(locator_type_by)
                locator_identifer = split_locator[1]
                ele = self.get_driver().find_elements(by=locator_type_by, value=locator_identifer)
            if self.get_driver().capabilities["platformName"] == "iOS":
                pstr_element_locator = split_type[1]
                split_locator = pstr_element_locator.split("=", 1)
                locator_type_by = self.get_by(split_locator[0])
                locator_identifer = split_locator[1]
                ele = self.get_driver().find_elements(by=locator_type_by, value=locator_identifer)
            return ele
        except Exception as e:
            raise Exception("Error occurred while getting the element :" + pstr_element_locator + "-->", e)

    def scroll(self, pstr_origin_element, pstr_destination_element, duration):
        try:
            origin_element = self.get_element(pstr_origin_element)
            destination_element = self.get_element(pstr_destination_element)
            self.get_driver().scroll(origin_element, destination_element, duration)
        except Exception as e:
            raise Exception("Exception occurred while scrolling element --> " + e)

    def switch_context(self, pstr_context_name):
        try:
            print("CONTEXTS INSIDE GET ELEMENT ARE ")
            current_context = self.get_driver().current_context
            self.wait_for_contexts_to_appear()
            if len(self.get_driver().contexts) > 1:
                self.get_driver().switch_to.context(pstr_context_name)
            print("CONTEXT SWITCHED TOO ", self.get_driver().context)
            return current_context
            # print(self.get_driver().contexts)
        except Exception as e:
            raise Exception("Exception occurred while switching context -->", str(e))

    def wait_for_contexts_to_appear(self):
        try:
            len_content = len(self.get_driver().contexts)
            count = 0
            while len_content < 2:
                len_content = len(self.get_driver().contexts)
                time.sleep(1)
                count += 1
                if count == 5:
                    break
            for i in self.get_driver().contexts:
                print(i)
        except Exception as e:
            raise Exception("Exception occurred while waiting for contexts to appear -->", e)

    def custom_hide_keyboard(self):
        try:
            self.get_driver().find_element(MobileBy.ACCESSIBILITY_ID, "Done").click()
            self.click_element("asd||xpath=//XCUIElementTypeOther//XCUIElementTypeButton[@name='Done']")
        except Exception as e:
            raise Exception("Exception occurred while custom hide keyboard -->", e)

    def press_enter_key(self, locator):
        try:
            self.get_element(locator).send_keys("\n")
        except Exception as e:
            raise Exception("Exception occurred while pressing enter key --->", e)

    def get_text(self, pstr_locator):
        try:
            return self.get_element(pstr_locator).text
        except Exception as e:
            raise Exception("Exception occurred while fetching text from element -->", e)

    def get_attribute_by_xyz(self, element: WebElement, attribute_string: str):
        att = element.get_attribute(attribute_string)
        return att

    def get_attribute_value(self, pstr_element_locator, attribute_value):
        try:
            print("INSIDE GET ELEMENT")
            val = ""
            split_type = pstr_element_locator.split("||")
            print(split_type)
            print("PLATFORM NAME IS")
            print(self.get_driver().capabilities["platformName"])
            if self.get_driver().capabilities["platformName"] == "Android":
                #print("INSIDE ANDROID GET ELEMENT")
                pstr_element_locator = split_type[0]
                #print(pstr_element_locator)
                split_locator = pstr_element_locator.split("=", 1)
                #print(split_locator)
                locator_type_by = self.get_by(split_locator[0])
                #print(locator_type_by)
                locator_identifer = split_locator[1]
                val = self.get_driver().find_element(by=locator_type_by, value=locator_identifer).get_attribute(
                    attribute_value)
            if self.get_driver().capabilities["platformName"] == "iOS":
                pstr_element_locator = split_type[1]
                split_locator = pstr_element_locator.split("=", 1)
                locator_type_by = self.get_by(split_locator[0])
                locator_identifer = split_locator[1]
                val = self.get_driver().find_element(by=locator_type_by, value=locator_identifer).get_attribute(
                    attribute_value)
            return val
        except Exception as e:
            raise Exception("Error occurred while getting the element :" + pstr_element_locator + "-->", e)

    def drag_and_drop(self, pstr_origin_element, pstr_target_element):
        try:
            origin_element = self.get_element(pstr_origin_element)
            destination_element = self.get_element(pstr_target_element)
            self.get_driver().drag_and_drop(origin_element, destination_element)
        except Exception as e:
            raise Exception("Exception occurred while scrolling element --> " + e)

    def element_is_displayed(self, pstr_element_locator):
        try:
            print("INSIDE GET ELEMENT")
            val = None
            split_type = pstr_element_locator.split("||")
            print(split_type)
            print("PLATFORM NAME IS")
            print(self.get_driver().capabilities["platformName"])
            if self.get_driver().capabilities["platformName"] == "Android":
                #print("INSIDE ANDROID GET ELEMENT")
                pstr_element_locator = split_type[0]
                #print(pstr_element_locator)
                split_locator = pstr_element_locator.split("=", 1)
                #print(split_locator)
                locator_type_by = self.get_by(split_locator[0])
                #print(locator_type_by)
                locator_identifier = split_locator[1]
                val = self.get_driver().find_element(by=locator_type_by, value=locator_identifier).is_displayed()
            if self.get_driver().capabilities["platformName"] == "iOS":
                pstr_element_locator = split_type[1]
                split_locator = pstr_element_locator.split("=", 1)
                locator_type_by = self.get_by(split_locator[0])
                locator_identifier = split_locator[1]
                val = self.get_driver().find_element(by=locator_type_by, value=locator_identifier).is_displayed()
            return val
        except Exception as e:
            return val
            #raise Exception("Error occurred while getting the element :" + pstr_element_locator + "-->", e)
