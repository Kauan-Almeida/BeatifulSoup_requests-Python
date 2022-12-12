'''
Para os imports funcionarem, primeiro fazer a instalação pelo prompt:
pip install requests
pip install beautifulsoup4
'''
import requests
from bs4 import BeautifulSoup
 
pagina = requests.get('http://www.uninove.br')
 
sopa = BeautifulSoup(pagina.text, 'html.parser')
 
# encontra todos os titulos
uninove = sopa.find_all('h1')
 
for i in uninove:
    print(i.prettify())
 
input('Tecle ENTER para sair...')
