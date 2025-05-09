import paramiko
import pandas as pd
import re
import os


class SwitchInterfaceStatusFetcher:
    def __init__(self, host, username, password, comando="show int status"):
        self.host = host
        self.username = username
        self.password = password
        self.comando = comando

    def conectar_e_extrair(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.host, username=self.username, password=self.password)

        stdin, stdout, stderr = ssh.exec_command(self.comando)
        saida = stdout.read().decode()
        ssh.close()

        return saida

    def processar_saida_para_dataframe(self, saida):
        linhas = saida.strip().split('\n')
        dados = []

        for linha in linhas[1:]:
            if linha.strip() == "":
                continue
            match = re.match(r'^(\S+)\s+(.+?)\s{2,}(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(.+)$', linha.strip())
            if match:
                dados.append(match.groups())

        df = pd.DataFrame(dados, columns=["Port", "Name", "Status", "Vlan", "Duplex", "Speed", "Type"])
        return df

    def obter_dataframe_com_ip(self):
        print(f"🔗 Conectando ao switch {self.host}...")
        saida = self.conectar_e_extrair()
        df = self.processar_saida_para_dataframe(saida)

        # Insere linha com o IP antes da tabela
        linha_ip = pd.DataFrame([[f"Switch: {self.host}"] + [""] * (df.shape[1] - 1)], columns=df.columns)
        df_com_ip = pd.concat([linha_ip, df], ignore_index=True)
        return df_com_ip


# Função utilitária para processar vários switches e salvar tudo em um único CSV
def salvar_todos_em_um_csv(switches, arquivo_saida="interfaces_todos_switches.csv"):
    df_total = pd.DataFrame()

    for switch in switches:
        df = switch.obter_dataframe_com_ip()
        df_total = pd.concat([df_total, df, pd.DataFrame([[""] * df.shape[1]], columns=df.columns)],
                             ignore_index=True)  # linha em branco

    df_total.to_csv(arquivo_saida, index=False)
    print(f"\n✅ Dados de todos os switches salvos em '{arquivo_saida}'")
