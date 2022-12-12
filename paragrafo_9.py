'''
Para os imports funcionarem, primeiro fazer a instalação pelo prompt:
pip install requests
pip install beautifulsoup4
'''
import requests
from bs4 import BeautifulSoup
 
pagina = requests.get("http://www.uninove.br")
 
sopa = BeautifulSoup(pagina.content, 'html.parser')
 
print(sopa.find_all('p')[2].get_text())
 
print(sopa.find_all('p')[4].get_text())
 
input('Tecle ENTER para sair...')

