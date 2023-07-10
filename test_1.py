import pytest


class Test1:

    #@pytest.mark.parametrize('all_browser', ['chrome'])
    def test_01(self, open_login_page):
        login_page = open_login_page
        #login_page.efetuar_login()

        # assert login_page.is_url_login(), "Aplicação não está na pagina de login!"
        # assert login_page.has_login_message_error(), "Mensagem de erro inválida!"
        #assert login_page.is_url_login(), "Aplicação não está na pagina de login!"
        assert open_login_page.efetuar_cadastro(), "Cadatrando usuãrio com sucesso."