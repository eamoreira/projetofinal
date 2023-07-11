from pages.filterpage import FilterPage


class Test6:

    def test_6(self, open_login_page):
        open_login_page.efetuar_login()
        catcompra = FilterPage(open_login_page.driver)
        assert catcompra.pesquisar_categoria(), "Filtro de produto por categoria realizada com sucesso."



