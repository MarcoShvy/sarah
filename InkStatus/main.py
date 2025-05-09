import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from impressora_HP_E50145 import coletar_status_tinta
import win32print

# Configurações de e-mail
EMAIL_REMETENTE = "email"
SENHA_EMAIL = "senha"
EMAIL_DESTINO = "informatica-LN@sarah.br"
SMTP_SERVER = "correio.sarah.br"
SMTP_PORT = 465

def enviar_email_alerta(assunto, mensagem):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_REMETENTE
        msg['To'] = EMAIL_DESTINO
        msg['Subject'] = assunto

        msg.attach(MIMEText(mensagem, 'plain'))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_REMETENTE, SENHA_EMAIL)
            server.send_message(msg)

        print("✅ E-mail de alerta enviado com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao enviar e-mail: {e}")


def listar_impressoras_com_ip(servidor="\\\\lnimp01"):
    impressoras = win32print.EnumPrinters(
        win32print.PRINTER_ENUM_NAME,
        servidor,
        2
    )

    lista_final = []
    impressora_a_ignorar = "HP Color LaserJet E55040 PCL 6 v3"

    for impressora in impressoras:
        nome_raw = impressora['pPrinterName']
        porta = impressora['pPortName']

        # Remove \\lnimp01\ do nome para melhor apresentação
        nome_limpo = re.sub(r"^\\\\[^\\]+\\", "", nome_raw).strip()

        # Ignora a impressora duplicada
        if nome_limpo == impressora_a_ignorar:
            continue

        ip_match = re.search(r"(10\.\d+\.\d+\.\d+)", porta)
        if ip_match:
            ip = ip_match.group(1)
            lista_final.append({
                "nome": nome_limpo,
                "ip": ip
            })

    return lista_final

impressoras = listar_impressoras_com_ip()

def verificar_impressoras_coloridas():
    alertas = []  # Armazenará os alertas para envio em um único e-mail

    for impressora in impressoras:
        nome = impressora["nome"]
        ip = impressora["ip"]

        print(f"\n📠 Impressora: {nome} ({ip})")
        cartuchos = coletar_status_tinta(ip)

        if not cartuchos:
            print("⚠️ Não foi possível coletar os dados.")
            continue

        for i, cartucho in enumerate(cartuchos):
            nivel_raw = cartucho['nivel'].replace('%', '').replace('*', '').replace('<', '').strip()

            if nivel_raw == "--":
                alerta_msg = f"🚨 ATENÇÃO: {nome} - {cartucho['cor']} está esgotando!"
                print(f"[{i}] {cartucho['cor']} | {cartucho['codigo']} | Nível: {cartucho['nivel']} {alerta_msg}")
                alertas.append(alerta_msg)
            else:
                try:
                    nivel_int = int(nivel_raw)
                    if nivel_int <= 10:
                        alerta_msg = f"⚠️ ATENÇÃO: {nome} - {cartucho['cor']} está com nível baixo ({nivel_int}%)"
                        print(
                            f"[{i}] {cartucho['cor']} | {cartucho['codigo']} | Nível: {cartucho['nivel']} - Nível baixo!")
                        alertas.append(alerta_msg)
                    else:
                        print(f"[{i}] {cartucho['cor']} | {cartucho['codigo']} | Nível: {cartucho['nivel']}")
                except ValueError:
                    print(
                        f"[{i}] {cartucho['cor']} | {cartucho['codigo']} | Nível: {cartucho['nivel']} - Erro ao ler nível")


    if alertas:
        assunto = "⚠️ ALERTA: Níveis de tinta baixos nas impressoras"
        mensagem = "Os seguintes cartuchos estão com níveis baixos:\n\n" + "\n".join(alertas)
        enviar_email_alerta(assunto, mensagem)

if __name__ == "__main__":
    verificar_impressoras_coloridas()