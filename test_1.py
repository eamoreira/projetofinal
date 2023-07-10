import pytest


class Test1:

    def test_01(self, open_login_page):
        assert open_login_page.efetuar_cadastro(), "Cadatrando usuário com sucesso."