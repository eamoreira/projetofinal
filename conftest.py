import time

import pytest
from pageobject.commands import send_keys
from paginas.loginpage import loginpage


@pytest.fixture()
def openlogin():
    login_page = loginpage()
    yield login_page




