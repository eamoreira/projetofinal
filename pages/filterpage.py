from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FilterPage:
    txt_product_name_expect = 'Stylish Dress'

    def __init__(self, driver):
        self.driver = driver

    def pesquisar_campo(self):
        self.driver.find_element(By.CSS_SELECTOR, '[href="/products"]').click() # Clicar no botão do menu "Products"

        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.visibility_of_element_located(
            (By.ID, 'search_product')))
        element.send_keys(self.txt_product_name_expect)
        self.driver.find_element(By.ID, 'submit_search').click() #Botão pesquisar
        return self.filter_success(self.txt_product_name_expect)

    def filter_success(self, expect_text):
        items = self.driver.find_elements(By.XPATH, "/html/body/section[2]/div/div/div[2]/div/div[2]")
        # Obtenha o nome do produto
        nome_produto = items[0].find_element(By.CSS_SELECTOR, "div.productinfo p").text
        # Verifique se apenas um item é retornado na lista
        return len(items) == 1 and nome_produto == expect_text

    def pesquisar_categoria(self):
        waitCategpry = WebDriverWait(self.driver, 5)
        elementCategory = waitCategpry.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[href="#Women"]')))  # codigo 25 a 27 é para esperar (Time.sleep)
        elementCategory.click()
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[href="/category_products/1"]'))) # codigo 25 a 27 é para esperar (Time.sleep)
        element.click()
        return self.find_category_success()

    def find_category_success(self):
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.visibility_of_element_located(
            (By.XPATH, '/html/body/section/div/div[2]/div[2]/div/div[2]/div/div[2]/ul/li/a')))  # codigo 25 a 27 é para esperar (Time.sleep)
        element.click()
        nome_produto = self.driver.find_element(By.XPATH, "/html/body/section/div/div/div[2]/div[2]/div[2]/div/h2").text
        return nome_produto == 'Sleeveless Dress'