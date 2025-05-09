import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def coletar_status_tinta(ip):
    url = f"https://{ip}/"
    try:
        response = requests.get(url, timeout=20, verify=False)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar na impressora: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    consumables = soup.find_all("div", class_="consumable")

    resultado = []
    for idx, item in enumerate(consumables):
        nome = item.find("h2", id=f"SupplyName{idx}")
        codigo = item.find("span", id=f"SupplyPartNumber{idx}")
        nivel = item.find("span", id=f"SupplyPLR{idx}")

        dados = {
            "cor": nome['title'] if nome and nome.has_attr('title') else "Desconhecido",
            "codigo": codigo['title'] if codigo and codigo.has_attr('title') else "Sem código",
            "nivel": nivel.text.strip() if nivel else "N/A"
        }

        resultado.append(dados)

    return resultado
