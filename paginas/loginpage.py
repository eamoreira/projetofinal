import string
import time
import random

from pageobject.commands import send_keys
from selenium import webdriver
from selenium.webdriver.common.by import By


class loginpage():
    url_cad = 'https://www.automationexercise.com/login'

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url_cad)



    def efetuar_login(self):
        self.driver.find_element(By).send_keys('')

    def efetuar_cadastro(self):
        random_value = ''.join(random.choice(string.ascii_letters) for _ in range(10))
        self.driver.find_element(By.XPATH, '/html/body/section/div/div/div[3]/div/form/input[2]').send_keys('teste projeto')  # CAMPO NOME
        self.driver.find_element(By.XPATH, '/html/body/section/div/div/div[3]/div/form/input[3]').send_keys(f'{random_value}@reitest.com') # CAMPO EMAIL
        self.driver.find_element(By.XPATH, '/html/body/section/div/div/div[3]/div/form/button').click()

        #DIRECIONADO PARA A FINALIZAÇÃO

        # INFORMAÇÕES DA CONTA

        self.driver.find_element(By.ID, 'id_gender1').click() # RADIO - GENERO FEMININO
        self.driver.find_element(By.ID, 'password').send_keys('12345678') # CAMPO SENHA
        self.driver.find_element(By.XPATH, '/html/body/section/div/div/div/div[1]/form/div[5]/div/div[1]/div/select/option[3]').click()  # CAMPO DIA (DATA DE NASCIMENTO)
        self.driver.find_element(By.XPATH, '/html/body/section/div/div/div/div[1]/form/div[5]/div/div[2]/div/select/option[3]').click()  # CAMPO MES (DATA DE NASCIMENTO)
        self.driver.find_element(By.XPATH, '/html/body/section/div/div/div/div[1]/form/div[5]/div/div[3]/div/select/option[28]').click() # CAMPO ANO (DATA DE NASCIMENTO)
        self.driver.find_element(By.ID, 'newsletter').click() #RADIO - newsletter
        self.driver.find_element(By.ID, 'optin').click() #RADIO - RECEBER OFERTAS ESPECIAIS## INFORMAÇÕES DE ENDEREÇO DE ENTREGA
        self.driver.find_element(By.ID, 'first_name').send_keys('Gustavo') #CAMPO Primeiro Nome
        self.driver.find_element(By.ID, 'last_name').send_keys('Dos Devs') #CAMPO Segundo nome
        self.driver.find_element(By.ID, 'address1').send_keys('Rua dos testadores, passa nada, Numº 12 - Recife') #Endereço 1
        self.driver.find_element(By.XPATH, '/html/body/section/div/div/div/div[1]/form/p[6]/select/option[3]').click() # SELECT - PAIS
        self.driver.find_element(By.ID, 'state').send_keys('Pernambuco') # Estado
        self.driver.find_element(By.ID, 'city').send_keys('Recife') # Cidade
        self.driver.find_element(By.ID, 'zipcode').send_keys('55555-555') #CEP
        self.driver.find_element(By.ID, 'mobile_number').send_keys('81 1111-7777') # TELEFONE
        time.sleep(5)
        self.driver.find_element(By.XPATH, '/html/body/section/div/div/div/div[1]/form/button').click() #Botão Criar cadastro






