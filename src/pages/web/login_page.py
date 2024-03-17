from src.pages.locators.web.login_locator import LoginPageLocators
from src.utils.bot_handlers.web_handler import WebHandler
from src.utils.config_handler import ConfigHandler


class WebLoginPage:

    def __init__(self):

        self.locators = LoginPageLocators()
        self.driver_handler = WebHandler()
        self.configs = ConfigHandler()

    def open_login_page(self):
        browser_url = self.configs.get_base_url_browser()
        self.driver_handler.open_url_in_browser(browser_url)
        
    # def enter_username(self, pstr_username):
    #     '''
    #     This method is used to click on edit button in claim page
    #     :return:
    #     '''
    #     try:
    #         self.driver_handler.send_keys(self.locators.w_email_textbox, pstr_username)
    #     except Exception as e:
    #         self.driver_handler.take_screen_shot("Error_username")
    #         raise Exception("Exception occured while entering username -->", e)

    # def enter_password(self, pstr_password):
    #     '''
    #     This method is used to click on edit button in claim page
    #     :return:
    #     '''
    #     try:
    #         self.driver_handler.send_keys(self.locators.w_password_textbox, pstr_password)
    #     except Exception as e:
    #         raise Exception("Exception occured while entering password -->", e)

    # def click_login_btn(self):
    #     '''
    #     This method is used to click on login button
    #     '''
    #     try:
    #         self.driver_handler.click_element(self.locators.w_login_btn)
    #     except Exception as e:
    #         raise Exception("Exception occured while clicking on login btn -->", e)

    # def navigate_to_login_page(self, login_page_for=None):
    #     """
    #     This method is used to navigate to login page
    #     """
    #     try:
    #         login_page_url = self.yaml_handler.get_base_url() if login_page_for is None else self.yaml_handler.get_base_url(
    #             login_page_for)
    #         self.driver_handler.get_url(login_page_url)
    #     except Exception as e:
    #         raise Exception("Exception occured while navigating to sensing login page -->", e)

    def login(self):
        """
        This method is used to perform login
        """
        try:
            username, password = self.yaml_handler.get_user_credentials()
            self.enter_username(username)
            self.enter_password(password)
            self.click_login_btn()
            self.driver_handler.take_screen_shot(name="login",attach_to_report=True)
        except Exception as e:
            raise Exception("Exception occurred while performing login -->", e)



    # def navigate_to_login_page_for_api(self):
    #     '''
    #     This method is used to navigate to login page for API Login
    #     '''
    #     try:
    #         self.driver_handler.get_driver().delete_all_cookies()
    #         self.driver_handler.get_url(self.yaml_handler.get_api_login_url())
    #         self.driver_handler.take_screen_shot()
    #     except Exception as e:
    #         raise Exception("Exception occured while navigating to avatar login page -->", e)
