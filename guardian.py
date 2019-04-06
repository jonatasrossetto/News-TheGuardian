import os
import requests 
import json
import pandas as pd #cria um acrônimo 'ps' para o nome da biblioteca 'pandas'

#limpando a tela no dos
os.system('cls' if os.name == 'nt' else 'clear')


url="https://content.guardianapis.com/search?api-key=cf99f715-ad44-4c9f-9a90-3b311bb4c32c"

print("acessando base de dados ...")
response=requests.get(url)
print(response)

if response.status_code==200: #código de resposta dizendo que o site está de pé!!!
    print("Hei, consegui acessar a base de dados!!!")
    print("agora estou buscando informações das notícias ...")
    dados=response.json() #desempacotar os dados em json na resposta da API
    #print(dados['response']['status']) #mostra o campo status de response
    #print(dados['response']['results'])
    dados2=dados['response']['results'] #seleciona somente a parte de notícias
    n=(len(dados2)) #quantidade de notícias em response
    
    #inc=0
    #print("usando while!!!")
    #while inc<10:
    #    dados3=dados['response']['results'][inc]
    #    print(inc)
    #    print(dados3['webTitle'])
    #    print(dados3['webUrl'])
    #    inc=inc+1
    #print("")
    #print("")
    #print("")
    titulo=list() #cria uma lista titulo zerada
    link=list() #cria uma lista link zerada
    print("usando for!!!")
    print("")
    for pos in dados2:
        print(pos['webTitle'])
        print(pos['webUrl'])
        titulo.append(pos['webTitle'])
        link.append(pos['webUrl'])
        print("---------------")
    df=pd.DataFrame({'Titulo':titulo, 'Link':link})
    df.to_csv("news.csv", index=False, sep=";", encoding='utf-8-sig') #encoding com conj de caracteres para não aparecer letras estranhas no excel

else:
    print("Alguma coisa deu errado e eu não consegui acessar a base de dados!!!")
    