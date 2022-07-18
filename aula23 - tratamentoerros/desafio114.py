# import urllib.requests            // Sem precisar baixar
import requests


url = 'http://pudim.com.br'

try:
    requests.get(url, timeout=5)
except BaseException:
    print('\033[31mO site do Pudim não está acessível no momento!\033[m')
else:
    print('\033[32mConsegui acessar o site do Pudim com sucesso!\033[m')
