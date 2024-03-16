from selenium import webdriver
from selenium.common import SessionNotCreatedException, SeleniumManagerException
from selenium.webdriver.chrome.service import Service as ChromeService
from src.utils.logger import logger
class BotSelenium:

    driver = None
    browser_name = None
    driver_path = None
    options = None

    def __init__(self, browser_on_tests_execute="chrome", driver_path=None):
        self.browser_name= browser_on_tests_execute
        self.driver_path= driver_path

        self.launch_browser()

    def open_url(self, url_to_open):
        self.driver.get(url=url_to_open)

    def launch_browser(self):
        try:
            if self.browser_name.lower() == 'chrome':
                if self.driver_path is not None:
                    try:
                        options = webdriver.ChromeOptions()
                        # TODO Moved these to some other place
                        #self.options.add_argument("--headless")
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
                        logger.error(f"Error while Launching browser, Please try to allow chrome from setting if you "
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
