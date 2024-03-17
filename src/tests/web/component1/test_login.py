import pytest
import sys, os

from src.pages.web.login_page import WebLoginPage
from conftest import BaseCase

sys.path.append(os.getcwd())
web_login = WebLoginPage()


@pytest.mark.web
class TestingDashboardDefault(BaseCase):

    def test_page_loading(self):
        web_login.open_login_page()
        page_url = web_login.get_page_url()
        assert page_url == "https://www.saucedemo.com/", f"Page URL is not matched after navigating, might be a redirected issue"

    def test_login(self):
        web_login.login()
        page_url = web_login.get_page_url()
        assert "inventory.html" in page_url
