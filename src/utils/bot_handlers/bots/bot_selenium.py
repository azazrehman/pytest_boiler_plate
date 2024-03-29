from selenium import webdriver
from selenium.common import SessionNotCreatedException, SeleniumManagerException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common import by
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as condition

from src.utils.logger import logger


class BotSelenium:
    driver = None
    browser_name = None
    driver_path = None
    options = None

    def __init__(self, browser_on_tests_execute="chrome", driver_path=None):
        self.browser_name = browser_on_tests_execute
        self.driver_path = driver_path

        self.launch_browser()

    def open_url(self, url_to_open):
        self.driver.get(url=url_to_open)

    def launch_browser(self):
        try:
            if self.driver is None:
                if self.browser_name.lower() == 'chrome':
                    if self.driver_path is not None:
                        try:
                            options = webdriver.ChromeOptions()
                            # TODO Moved these to some other place
                            # self.options.add_argument("--headless")
                            options.add_argument('--no-sandbox')
                            options.add_argument('--disable-dev-shm-usage')
                            options.add_argument('--window-size=1600,900')
                            service = ChromeService(executable_path=self.driver_path)
                            self.driver = webdriver.Chrome(service=service, options=options)
                        except SessionNotCreatedException as sne:
                            logger.warning(f"There is Session not created Error with following below message, We are "
                                           f"trying to open browser without driver path {sne}")
                            self.driver = webdriver.Chrome()
                        except SeleniumManagerException as sme:
                            logger.error(
                                f"Error while Launching browser, Please try to allow chrome from setting if you "
                                f"are using it in first time at mac - Detail {sme}")
                            raise

                    else:
                        self.driver = webdriver.Chrome()
                elif self.browser_name.lower() == 'firefox':
                    self.driver = webdriver.Firefox()
        except Exception as e:
            logger.error(
                f"Error while Launching browser {e}")
            raise

    def quit_browser(self):
        self.driver.quit()
        self.driver = None

    def get_url(self):
        return self.driver.current_url

    def take_and_save_screenshot(self, directory_path):
        self.driver.save_screenshot(directory_path)

    def get_element(self, pstr_locator, pint_explicit_wait, pbool_with_exception=True):
        try:
            element = WebDriverWait(self.driver, pint_explicit_wait).until(
                condition.presence_of_element_located((by.By.XPATH, pstr_locator))
            )
            return element
        except Exception as e:
            if pbool_with_exception is True:
                raise Exception("Error occurred while getting the element :" + pstr_locator + "-->", e)
            else:
                return None

    def wait_for_locator(self, pstr_locator, pint_waiting_time, waiting_state="visible"):
        if waiting_state == "visible":
            WebDriverWait(self.driver, pint_waiting_time).until(
                condition.visibility_of(self.get_element(pstr_locator, pint_waiting_time)))

    def click_element(self, pstr_locator, pint_waiting_time):
        element = self.get_element(pstr_locator, pint_waiting_time)
        element.click()

    def type_text(self, pstr_locator, pint_waiting_time, pstr_text):
        element = self.get_element(pstr_locator, pint_waiting_time)
        element.send_keys(pstr_text)
