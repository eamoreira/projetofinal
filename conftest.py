import pytest

from pages.LoginPage import LoginPage

def pytest_addoption(parser):
    parser.addoption("--browser", default='chrome', help='Browser to run the tests.')

@pytest.fixture()
def open_login_page():
    # login_page = LoginPage()
    # yield login_page
    login_page = LoginPage()
    yield login_page
    #login_page.save_screenshot_page()
    #login_page.close()




