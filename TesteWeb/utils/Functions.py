from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import keyboard
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class Functions:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.actions = ActionChains(self.driver)

    def clicar(self, by, locator):
        self.wait.until(EC.element_to_be_clickable((by, locator))).click()

    def digitar(self, by, locator, texto):
        self.clicar(by, locator)
        time.sleep(1)
        keyboard.write(texto,delay=0.15)
        keyboard.send("enter")

    def digitar_texto(self, by, locator, texto):
        campo = self.wait.until(EC.visibility_of_element_located((by, locator)))
        campo.clear()
        campo.send_keys(texto)


    def localizar_elemento_e_clicar(self, by, locator):
        self.esperar_elemento_carregar()
        self.esperar_elemento_clicavel(by, locator)
        self.wait.until_not(EC.visibility_of_element_located((By.CLASS_NAME, "q-loading__backdrop")))
        elemento = self.wait.until(EC.visibility_of_element_located((by,locator)))
        elemento.click()

    def esperar_elemento_com_refresh(self, by, locator, tentativas=5):

        for _ in range(tentativas):
            try:
                self.wait.until(EC.visibility_of_element_located((by, locator)))
                return
            except:
                self.driver.refresh()
                time.sleep(2)

    def esperar_elemento_carregar(self):
        self.wait.until_not(EC.visibility_of_element_located((By.CLASS_NAME, "q-spinner q-spinner-mat q-loading__spinner")))
        sleep(1)
        self.wait.until_not(EC.visibility_of_element_located((By.CLASS_NAME, "q-spinner q-spinner-mat q-loading__spinner")))


    def esperar_elemento_clicavel(self, by, locator,):
        elemento = self.wait.until(EC.element_to_be_clickable((by, locator)))

    def selecionar_horario_19(self):
        horario = self.driver.find_element(By.XPATH, '//div[@class="q-chip__content col row no-wrap items-center q-anchor--skip" and text()=" + 17:00"]')
        self.driver.execute_script("arguments[0].scrollIntoView();", horario)
        self.driver.execute_script("arguments[0].click();", horario)

    def clicar_botao_quadro_vaga(self):
        horario = self.driver.find_element(By.XPATH,"//*[@id='q-app']/div/div/div[2]/main/div/div[2]/div[2]/div[2]/div/div/div[3]/div/div[1]/button[2]")
        self.driver.execute_script("arguments[0].click();", horario)

    def adicionar_mais_vaga(self):
        self.esperar_elemento_carregar()
        elemento = self.driver.find_element(By.XPATH, "//*[@id='q-app']/div/div/div[2]/main/div/div[2]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div[1]/label/div/div[1]/div[3]/button")
        self.driver.execute_script("arguments[0].click();", elemento)


    def selecionar_forma_presencial(self):
        self.esperar_elemento_carregar()
        elemento = self.driver.find_element(By.XPATH,
                                            "//*[@id='q-app']/div/div/div[2]/main/div/div[2]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div[2]/div[1]/label/div/div[1]/div[1]/div[2]/button[1]")
        self.driver.execute_script("arguments[0].click();", elemento)

    def selecionar_atuacao(self, nome):
        self.esperar_elemento_carregar()
        primeira = self.driver.find_element(By.CSS_SELECTOR, ".common__janela__evento > div:first-child")
        input_element = primeira.find_element(By.CSS_SELECTOR, "input")

        # Escrever no campo
        input_element.send_keys(nome)
        time.sleep(2)
        input_element.send_keys(Keys.ARROW_DOWN)
        input_element.send_keys(Keys.ENTER)

    def selecionar_consulta(self, nome):
        self.esperar_elemento_carregar()
        keyboard.send("tab")
        keyboard.send("tab")
        keyboard.write(nome)
        sleep(0.5)
        keyboard.send("down")
        sleep(0.5)
        keyboard.send("enter")

    def botao_incluir(self):
        botao = self.driver.find_element(By.XPATH,"//*[@id='q-app']/div/div/div[2]/main/div/div[2]/div[2]/div[2]/div/div/div[4]/button[2]")
        self.driver.execute_script("arguments[0].click();", botao)

    def botao_repetir(self):
        botao = self.driver.find_element(By.XPATH, '//*[@id="q-app"]/div/div/div[2]/main/div/div[2]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[2]/div[1]/div[2]')
        self.driver.execute_script("arguments[0].click();", botao)