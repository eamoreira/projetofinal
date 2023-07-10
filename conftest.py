import pytest

from pages.LoginPage import LoginPage

@pytest.fixture()
def open_login_page():
    login_page = LoginPage()
    yield login_page




