from pages.ShoppingPage import ShoppingPage

class Test4:

    def test_4(self, open_login_page):
        open_login_page.efetuar_login()
        retornarprod = ShoppingPage(open_login_page.driver)
        retornarprod.detalhe_item()
        assert retornarprod.remover_carrinho(), "Item removido do carrinho com sucesso."
