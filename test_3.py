from pages.ShoppingPage import ShoppingPage

class Test3:
    def test_3(self, open_login_page):
        open_login_page.efetuar_login()
        valores = ShoppingPage(open_login_page.driver)
        valores.detalhe_item()
        assert valores.payment(), "Pagamento realizado com sucesso."
