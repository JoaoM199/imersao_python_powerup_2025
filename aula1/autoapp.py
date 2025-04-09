import pyautogui
import pandas as pd
import time
from dotenv import load_dotenv
import os

load_dotenv()
username = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

site = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

# Passo 1 - Entrar no sistema da empresa
pyautogui.press('win')
pyautogui.write('edge')
pyautogui.press('enter')

# Acessar site
time.sleep(1)     # Espera meio segundo
pyautogui.write(site)
pyautogui.press('enter')

time.sleep(1)

# Passo 2 - Fazer login
pyautogui.click(x=664, y=364)
pyautogui.write(username)
pyautogui.press('tab')
pyautogui.write(password)
pyautogui.press('tab')
pyautogui.press('enter')

# Passo 3 - Importar base de dados
produtos = pd.read_csv("produtos.csv")
print(produtos)

# Passo 4 - Cadastrar produtos
for linha in produtos.index:
    pyautogui.click(x=713, y=241)
    codigo = produtos.loc[linha, "codigo"]
    pyautogui.write(codigo)
    time.sleep(0.5)

    pyautogui.press('tab')
    marca = produtos.loc[linha, "marca"]
    pyautogui.write(marca)
    time.sleep(0.5)

    pyautogui.press('tab')
    tipo = produtos.loc[linha, "tipo"]
    pyautogui.write(tipo)
    time.sleep(0.5)

    pyautogui.press('tab')
    categoria = str(produtos.loc[linha, "categoria"]) # Número para caractere
    pyautogui.write(categoria)
    time.sleep(0.5)

    pyautogui.press('tab')
    preco_unitario = str(produtos.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    time.sleep(0.5)

    pyautogui.press('tab')
    custo = str(produtos.loc[linha, "custo"])
    pyautogui.write(custo)
    time.sleep(0.5)

    pyautogui.press('tab')
    obs = str(produtos.loc[linha, "obs"])
    print(obs)
    if obs != "nan":
        pyautogui.write(obs)
    time.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(10000)