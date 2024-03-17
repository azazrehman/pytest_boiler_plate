from src.pages.locators.web.login_page_locators import LoginPageLocators
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
    def get_page_url(self):
        page_url = self.driver_handler.get_page_url()
        return page_url
    def login(self):
        """
        This method is used to perform login
        """
        try:
            self.open_login_page()
            self.driver_handler.type_text(self.locators.w_email_textbox,'standard_user')
            self.driver_handler.type_text(self.locators.w_password_textbox, 'secret_sauce')
            self.driver_handler.click(self.locators.w_login_btn)
            # username, password = self.yaml_handler.get_user_credentials()

        except Exception as e:
            raise Exception("Exception occurred while performing login -->", e)
