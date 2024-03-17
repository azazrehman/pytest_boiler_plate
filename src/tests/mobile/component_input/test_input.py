import os,sys
sys.path.append(os.getcwd())

from src.utils.bot_handlers.web_handler import WebHandler

web_handler = WebHandler()
class TestInputField:

    def test_enter_values():
        web_handler.open_url_in_browser('https://www.google.com')
        print(f"My First Test")