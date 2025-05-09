import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.Functions import Functions
import time

driver = webdriver.Chrome()
driver.get("https://bsbwebhomo.sarah.br/catalogoSistemas/#/")
driver.maximize_window()
for i in range(5):
    driver.refresh()
    time.sleep(0.5)
funcoes = Functions(driver)

def iniciar_SIH_web():

    try:
        iframe = driver.find_element(By.ID, "auth_callback")
        driver.switch_to.frame(iframe)
        # clicar botao continuar como
        funcoes.localizar_elemento_e_clicar(By.ID, "nmwin")

        driver.switch_to.default_content()
        # fechar botao de tutorial catalago
        funcoes.localizar_elemento_e_clicar(By.CLASS_NAME, "driver-close-btn")
        # clicar na aba hospitalar
        funcoes.localizar_elemento_e_clicar(By.XPATH, '//*[@id="q-app"]/div/div/div[2]/main/div[1]/nav/div/div/div/div[2]')
        # clicar em SIH WEB
        funcoes.localizar_elemento_e_clicar(By.XPATH, "//div[contains(text(), 'SIH WEB')]")
        driver.switch_to.window(driver.window_handles[-1])
        # clica no botao Paciente
        funcoes.esperar_elemento_clicavel(By.XPATH, '//*[@id="q-app"]/div/div/div[2]/main/div/div[2]/div[1]/div[1]/div/button[2]')
        funcoes.localizar_elemento_e_clicar(By.XPATH, '//*[@id="q-app"]/div/div/div[2]/main/div/div[2]/div[1]/div[1]/div/button[2]')
        time.sleep(2)
        # Digita prontuario do paciente
        funcoes.digitar(By.XPATH, "//*[@id='q-app']/div/div/div[2]/main/div/div[2]/div[1]/div[1]/div/label/div/div/div[3]/i", "D999999")
        time.sleep(2)
        keyboard.send('down')
        keyboard.send('enter')

        # Seleciona fixamente o horario de 19 horas do dia atual
        time.sleep(3)
        funcoes.selecionar_horario_19()

        time.sleep(5)
        # Clica no botão quadro vaga na janela de incluir novo evento
        funcoes.clicar_botao_quadro_vaga()



        funcoes.adicionar_mais_vaga()
        funcoes.selecionar_forma_presencial()

        funcoes.selecionar_atuacao("Analista Tauil")
        funcoes.selecionar_consulta("Grupo Interativo de Pacientes LM - LN - Geral")
        time.sleep(2)
        funcoes.botao_incluir()


        input("enter")
    except Exception as e:
        print(e)





iniciar_SIH_web()
