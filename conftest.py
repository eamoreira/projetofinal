import pytest

from pages.LoginPage import LoginPage
from pages.UserRegistrationPage import UserRegistrationPage


@pytest.fixture()
def open_login_page():
    login_page = LoginPage()
    yield login_page

@pytest.fixture()
def open_registration_page():
    registrationPage = UserRegistrationPage()
    yield registrationPage




