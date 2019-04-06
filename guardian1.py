import os
import requests 
import json
import pandas as pd #cria um acrônimo 'ps' para o nome da biblioteca 'pandas'

def limpatela():
    os.system('cls' if os.name == 'nt' else 'clear') #limpando a tela no dos

def searchnews(subject,news): #realiza a pesquisa de noticiais sobre subject
    titulo=list()
    link=list()
    #print(news)
    for pos in news:
        if pos['pillarName'] == subject:
            print(pos['pillarName'])
            titulo.append(pos['webTitle'])
            link.append(pos['webUrl'])
    return(titulo,link)

def exportar_csv(nome,t,l): #salva um arquivo tipo csv com dados especificados em t e l
    df=pd.DataFrame({'Titulo':t, 'Link':l})
    df.to_csv("%s.csv" %nome, index=False, sep=";", encoding='utf-8-sig') #encoding com conj de caracteres para não aparecer letras estranhas no excel
    print("arquivo exportado!!!!")

def getnews():
    url="https://content.guardianapis.com/search?api-key=cf99f715-ad44-4c9f-9a90-3b311bb4c32c"
    print("acessando base de dados ...")
    response=requests.get(url)
    if response.status_code==200: #código de resposta dizendo que o site está de pé!!!
        print("Hei, consegui acessar a base de dados!!!")
        print("agora estou buscando informações das notícias ...")
        dados=response.json() #desempacotar os dados em json na resposta da API
        saida=dados['response']['results'] #seleciona somente a parte de notícias
        return(saida)
    else:
        print("Alguma coisa deu errado")
        quit()

def main(): #função principal
    limpatela()
    dados2=getnews()
    artes=searchnews('Arts',dados2)
    esportes=searchnews('Sport',dados2)
    noticias=searchnews('News',dados2)
    exportar_csv("artes",artes[:][0],artes[:][1])
    exportar_csv("esportes",esportes[:][0],esportes[:][1])
    exportar_csv("noticias",noticias[:][0],noticias[:][1])

if __name__ == "__main__":
    main()