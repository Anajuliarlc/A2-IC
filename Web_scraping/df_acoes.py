from bs4 import BeautifulSoup #Biblioteca para achar tags html, depois vamos colocar num dataframe do pandas
import pandas as pd #Biblioteca para guardar data frame
import requests #Biblioteca para extrair uma URL

#WebScraping
#Url do html
url = "https://zuilhose.github.io/A2-Intro-Comp/"
# Obtendo o conteúdo da página em formato de texto

data = requests.get(url).text
soup = BeautifulSoup(data,"html.parser")

#Procurando divs com classes:
div_acao = soup.find("div", class_ = "acao")

# Procurando as tabelas por classe na página
table_class_acoes = div_acao.find("table") # tabela de ações

# Definindo dataframe
#aqui por enquanto só definimos as colunas
df_acoes = pd.DataFrame(columns=["Ação", "Quantidade"]) #dataframe da tabela ações

#Contando o número de linhas em cada tabela
linhas_na_tabela_acoes = [] #Aqui vamos por um item para linha da tabela com dados, para conseguir o número de linhas
for row in table_class_acoes.find_all("tr"):# em html uma linha da tabela é representada pela tag <tr>
    columns_acoes = row.find_all("td") # em html uma coluna da tabela é representada pela tag <td>
    if (columns_acoes!= []):
        linhas_na_tabela_acoes.append("linha")
num_linhas_acoes = len(linhas_na_tabela_acoes) #número de linhas em tabela ações
#Obtendo todas as linhas da tabela
        #Obtendo todas as linhas da tabela acoes

for row in table_class_acoes.find_all("tr"): # em html uma linha da tabela é representada pela tag <tr>
    # Obtendo todas as colunas em cada linha
    columns_acoes = row.find_all("td")  # em html uma coluna da tabela é representada pela tag <td>

    if (columns_acoes != []):
        acao = columns_acoes[0].text.strip(" ")
        quantidade = columns_acoes[1].text.strip(" ")
        df_acoes = pd.concat([df_acoes, pd.DataFrame.from_records([{"Ação": acao, "Quantidade": quantidade}])], ignore_index=True)
        # Aqui a primeira linha vai conter o nosso primeiro df_acoes definido que contém Ação, Quantidade, ou seja os nomes das nossas colunas
        # a segunda parte dos nossos dados serão achados pelo método pandas.DataFrame.from_records
        # nele teremos uma lista é claro, pois em cada linha temos mais de uma informação
        # nesta lista queremos a ação e a quantidade o que a gente tem!
        # pois definimos acao e quantidade
        # Podemos usar o método com dicionário! a chave do dic é a coluna e o valor é o que a coluna vai receber, no caso acao e quantidade IZI
        # o ignore_index é para enumerar nossas linhas, note que ele não coloca numero em ação e quantidade, pois definimos esse dado como coluna

df_acoes.head(num_linhas_acoes) #Para retornar as num_linhas_acoes desejadas

# Refatorando o dataframe
#Aqui só vou arrumar os dados para ficar da forma certa, pois tratamos eles como str, mas não necessariamente são str
    #Ações
        # Ação
df_acoes["Ação"] = df_acoes["Ação"].str.upper()
        # Quantidade
df_acoes["Quantidade"] = [x.replace(',', '.') for x in df_acoes["Quantidade"]]
df_acoes = df_acoes.astype({"Quantidade": float})

df_acoes.head(num_linhas_acoes)

print(df_acoes.head(num_linhas_acoes))

