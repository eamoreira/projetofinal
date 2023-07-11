from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class ShoppingPage:
    txt_expect_success = 'Proceed To Checkout'
    txt_expect_payment_success = 'ORDER PLACED!'
    txt_expect_remove_cart_success = 'Cart is empty!'
    def __init__(self, driver):
        self.driver = driver

    def detalhe_item(self):
        # detalhe do pedido e adicionar ao carrinho
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[href="/product_details/1"]')))  # codigo 25 a 27 é para esperar (Time.sleep)
        element.click()

        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                               '/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/button')))  # codigo 25 a 27 é para esperar (Time.sleep)
        element.click()
        self.driver.find_element(By.CSS_SELECTOR, '[href="/view_cart"]').click()  # Clicar em ver o carrinho
        return self.details_success(self.txt_expect_success)

    def details_success(self, expect_text):
        return self.driver.find_element(By.CSS_SELECTOR, 'a.btn.btn-default.check_out').text == expect_text

    def payment(self):
        self.driver.find_element(By.XPATH, '//*[@id="do_action"]/div[1]/div/div/a').click()  # Continuar para pagamento
        self.driver.find_element(By.CSS_SELECTOR, '[href="/payment"]').click()  # Realizar pagamento

        # dados do cartão
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[name="name_on_card"]')))  # espera aparecer o campo de select para poder clicar
        element.send_keys('joao dos testes')
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[name="card_number"]')))  # espera aparecer o campo de select para poder clicar
        element.send_keys('2222333344445555')
        self.driver.find_element(By.CSS_SELECTOR, '[name="cvc"]').send_keys('333')  # cvc do cartão
        self.driver.find_element(By.CSS_SELECTOR, '[name="expiry_month"]').send_keys('06')  # Mes de vencimento
        self.driver.find_element(By.CSS_SELECTOR, '[name="expiry_year"]').send_keys('2024')  # ano de vencimento
        self.driver.find_element(By.ID, 'submit').click()  # Botão finalizar pagamento
        return self.payment_success(self.txt_expect_payment_success)

    def payment_success(self, expect_text):
        return self.driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/h2/b').text == expect_text

    def remover_carrinho(self):
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, 'fa-times')))  # espera aparecer o campo de select para poder clicar
        element.click()
        return self.remove_success(self.txt_expect_remove_cart_success)

    def remove_success(self, expect_text):
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="empty_cart"]/p/b')))
        return element.text == expect_text
