from pages.ShoppingPage import ShoppingPage
class Test2:

    def test_compras(self, open_login_page):
        open_login_page.efetuar_login()
        compras = ShoppingPage(open_login_page.driver)
        assert compras.detalhe_item(), "Detalhes do produto exibido com sucesso."

