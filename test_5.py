from pages.filterpage import FilterPage

class Test5:

    def test_05(self, open_login_page):
        open_login_page.efetuar_login()
        pesquisarprod = FilterPage(open_login_page.driver)
        assert pesquisarprod.pesquisar_campo(), "Pesquisa por produto realizada com sucesso."