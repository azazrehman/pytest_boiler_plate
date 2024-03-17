import pytest
import sys, os

from src.pages.web.login_page import WebLoginPage
from conftest import BaseCase

sys.path.append(os.getcwd())
web_login = WebLoginPage()


@pytest.mark.web
class TestingDashboardDefault(BaseCase):

    def test_login_site(self):
        web_login.open_login_page()
