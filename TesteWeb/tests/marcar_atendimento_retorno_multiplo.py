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
        print("Clicou botar continuar como")
        driver.switch_to.default_content()
        # fechar botao de tutorial catalago
        funcoes.localizar_elemento_e_clicar(By.CLASS_NAME, "driver-close-btn")
        print("Fechou botao de tutorial do catalogo")
        # clicar na aba hospitalar
        funcoes.localizar_elemento_e_clicar(By.XPATH, '//*[@id="q-app"]/div/div/div[2]/main/div[1]/nav/div/div/div/div[2]')
        print("Abriu aba hospitalar")
        # clicar em SIH WEB
        funcoes.localizar_elemento_e_clicar(By.XPATH, "//div[contains(text(), 'SIH WEB')]")
        driver.switch_to.window(driver.window_handles[-1])
        print("Abriu SIH WEB")
        # clica no botao Paciente
        funcoes.esperar_elemento_clicavel(By.XPATH, '//*[@id="q-app"]/div/div/div[2]/main/div/div[2]/div[1]/div[1]/div/button[2]')
        funcoes.localizar_elemento_e_clicar(By.XPATH, '//*[@id="q-app"]/div/div/div[2]/main/div/div[2]/div[1]/div[1]/div/button[2]')
        print("clicou na aba paciente")
        time.sleep(2)
        # Digita prontuario do paciente
        funcoes.digitar(By.XPATH, "//*[@id='q-app']/div/div/div[2]/main/div/div[2]/div[1]/div[1]/div/label/div/div/div[3]/i", "D999999")
        time.sleep(2)
        keyboard.send('down')
        keyboard.send('enter')
        print("Digitou prontuario e abriu")

        # Seleciona fixamente o horario de 19 horas do dia atual
        time.sleep(3)
        funcoes.selecionar_horario_19()
        print("Selecionou horario 19 horas")
        time.sleep(5)
        # Clica no botão quadro vaga na janela de incluir novo evento
        funcoes.clicar_botao_quadro_vaga()
        print("Abriu aba de incluir novo evento")



        funcoes.adicionar_mais_vaga()
        print("Adicionou uma vaga")
        funcoes.selecionar_forma_presencial()
        print("Selecionou forma presencial")
        funcoes.botao_repetir()
        print("Apertou botao para retorno multiplo")


        funcoes.selecionar_atuacao("Analista Tauil")
        print("Selecionou profissional")
        funcoes.selecionar_consulta("Grupo Interativo de Pacientes LM - LN - Geral")
        print("Selecionou consulta")
        time.sleep(2)

        janela = driver.find_element(By.CLASS_NAME, "common__janela__corpo__scroll")
        driver.execute_script("arguments[0].scrollIntoView();", janela)
        funcoes.localizar_elemento_e_clicar(By.ID, "f_fd0b4f4f-eb1d-435d-95d1-76785dc345c1")
        funcoes.localizar_elemento_e_clicar(By.ID, "f_fd0b4f4f-eb1d-435d-95d1-76785dc345c1_1")

        input("enter")

    except Exception as e:
        print(e)

iniciar_SIH_web()