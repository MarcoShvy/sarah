from selenium import webdriver
from selenium.webdriver.common.by import By
from Functions import Functions
import time

def Iniciar_SIH_Web():
    driver = webdriver.Chrome()
    driver.get("https://bsbwebhomo.sarah.br/catalogoSistemas/#/")
    driver.maximize_window()
    for i in range(5):
        driver.refresh()
        time.sleep(0.5)
    funcoes = Functions(driver)

    iframe = driver.find_element(By.ID, "auth_callback")
    driver.switch_to.frame(iframe)

    funcoes.localizar_elemento_e_clicar(By.ID, "nmwin")

    driver.switch_to.default_content()

    funcoes.localizar_elemento_e_clicar(By.CLASS_NAME, "driver-close-btn")

    funcoes.localizar_elemento_e_clicar(By.XPATH, '//*[@id="q-app"]/div/div/div[2]/main/div[1]/nav/div/div/div/div[2]')

    funcoes.localizar_elemento_e_clicar(By.XPATH, "//div[contains(text(), 'SIH WEB')]")
