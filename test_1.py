import pytest


class Test1:

    def test_01(self, open_registration_page):
        assert open_registration_page.register(), "Cadatrando usuário com sucesso."