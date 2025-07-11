import requests
from bs4 import BeautifulSoup

def buscar_produtos(termo):
    url = f"https://lista.mercadolivre.com.br/{termo.replace(' ', '-')}"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    resultados = []
    for item in soup.select('.ui-search-result')[:10]:
        nome = item.h2.text.strip()
        preco = item.select_one('.price-tag-fraction')
        preco = preco.text.strip() if preco else 'N/A'
        link = item.a['href']
        resultados.append({'nome': nome, 'preco': preco, 'link': link})
    return resultados
