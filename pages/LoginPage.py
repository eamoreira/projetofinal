import string
import random

from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class LoginPage(PageObject):
    url_login = 'https://www.automationexercise.com/login'
    id_username = 'user-name'
    id_password = 'password'
    txt_success = 'Congratulations! Your new account has been successfully created!'

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url_login)

    def efetuar_login(self):
        self.driver.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys('fcb@gmail.com')
        self.driver.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys('1234')
        self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    def is_url_login(self):
        return self.is_url(url=self.url_login)

    def efetuar_cadastro(self):
        random_value = ''.join(random.choice(string.ascii_letters) for _ in range(10))
        # //*[@id="form"]/div/div/div[3]/div/form/input[2]
        self.driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/input[2]').send_keys(
            'teste projeto')  # CAMPO NOME
        self.driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/input[3]').send_keys(
            f'{random_value}@reitest.com')  # CAMPO EMAIL
        self.driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/button').click()

        # DIRECIONADO PARA A FINALIZAÇÃO

        # INFORMAÇÕES DA CONTA

        self.driver.find_element(By.ID, 'id_gender1').click()  # RADIO - GENERO FEMININO
        self.driver.find_element(By.ID, 'password').send_keys('12345678')  # CAMPO SENHA
        self.driver.find_element(By.XPATH,
                                 '/html/body/section/div/div/div/div[1]/form/div[5]/div/div[1]/div/select/option[3]').click()  # CAMPO DIA (DATA DE NASCIMENTO)
        self.driver.find_element(By.XPATH,
                                 '/html/body/section/div/div/div/div[1]/form/div[5]/div/div[2]/div/select/option[3]').click()  # CAMPO MES (DATA DE NASCIMENTO)
        self.driver.find_element(By.XPATH,
                                 '/html/body/section/div/div/div/div[1]/form/div[5]/div/div[3]/div/select/option[28]').click()  # CAMPO ANO (DATA DE NASCIMENTO)
        self.driver.find_element(By.ID, 'first_name').send_keys('Gustavo')  # CAMPO Primeiro Nome
        self.driver.find_element(By.ID, 'last_name').send_keys('Dos Devs')  # CAMPO Segundo nome
        self.driver.find_element(By.ID, 'address1').send_keys(
            'Rua dos testadores, passa nada, Numº 12 - Recife')  # Endereço 1
        self.driver.find_element(By.XPATH,
                                 '/html/body/section/div/div/div/div[1]/form/p[6]/select/option[3]').click()  # SELECT - PAIS
        self.driver.find_element(By.ID, 'state').send_keys('Pernambuco')  # Estado
        self.driver.find_element(By.ID, 'city').send_keys('Recife')  # Cidade
        self.driver.find_element(By.ID, 'zipcode').send_keys('55555-555')  # CEP
        self.driver.find_element(By.ID, 'mobile_number').send_keys('81 1111-7777')  # TELEFONE

        button = self.driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/div[1]/form/button')
        self.driver.execute_script("arguments[0].click();", button)
        return self.is_success(self.txt_success)

    def is_success(self, text_title):
        return self.driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/p[1]').text == text_title
