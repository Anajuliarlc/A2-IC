import openpyxl
from bs4 import BeautifulSoup #Biblioteca para achar tags html, depois vamos colocar num dataframe do pandas
import numpy as np
import pandas as pd #Biblioteca para guardar data frame
import requests #Biblioteca para extrair uma URL



#WebScraping
#Url do html
url = "https://anajuliarlc.github.io/Trabalho-de-IC/sitecar/carteira%201"
# Obtendo o conteúdo da página em formato de texto

data = requests.get(url).text
soup = BeautifulSoup(data,"html.parser")
#Procurando divs com classes:
div_acao = soup.find("div", class_ = "acao")
div_moeda = soup.find("div", class_ = "moeda")

# Procurando as tabelas por classe na página
table_class_acoes = div_acao.find("table") # tabela de ações
table_class_moedas = div_moeda.find("table") # tabela de moedas

# Definindo dataframe
df_acoes = pd.DataFrame(columns=["Ação", "Valor"]) #dataframe da tabela ações
df_moedas = pd.DataFrame(columns=["Moeda", "Capital"]) #dataframe da tabela moedas
    #Contando o número de linhas em cada tabela
num_linhas_acoes = len(table_class_acoes.tbody.find_all("tr")) #número de linhas em tabela ações
num_linhas_moedas = len(table_class_moedas.tbody.find_all("tr")) #némero de linhas em tabela moedas
#Obtendo todas as linhas da tabela
        #Obtendo todas as linhas da tabela moedas
for row in table_class_acoes.tbody.find_all("tr"):
    # Obtendo todas as colunas em cada linha
    columns = row.find_all("td")  # em html uma coluna da tabela é representada pela tag <td>
    if (columns != []):
        acao = columns[0].text.strip(" ")
        capital = columns[1].text.strip(" ")
        df_acoes = pd.concat([df_acoes, pd.DataFrame.from_records([{"Ação": acao, "Capital": capital}])], ignore_index=True)
df_acoes.head(num_linhas_acoes)

    # Obtendo todas as linhas da tabela acoes
for row in table_class_moedas.tbody.find_all("tr"):  # em html uma linha da tabela é representada pela tag <tr>
    # Obtendo todas as colunas em cada linha
    columns = row.find_all("td")  # em html uma coluna da tabela é representada pela tag <td>
    if (columns != []):
        moeda = columns[0].text.strip(" ")
        quantidade = columns[1].text.strip(" ")
        df_moedas = pd.concat([df_moedas, pd.DataFrame.from_records([{"Moedas": moeda, "Valor": quantidade}])], ignore_index=True)
df_moedas.head(num_linhas_moedas)
print(df_moedas.head(num_linhas_moedas))
# Refatorando o dataframe

    #Ações
        # Ação
df_acoes["Ação"] = df_acoes["Ação"].str.upper()
        # Valor
df_acoes["Capital"] = [x.replace(',', '.') for x in df_acoes["Capital"]]
df_acoes = df_acoes.astype({"Valor": float})

df_acoes.head(num_linhas_acoes)
    # Moeda
df_moedas["Moeda"] = df_moedas["Moeda"].str.upper()
        # Valor
df_moedas["Valor"] = [x.replace(',', '.') for x in df_moedas["Valor"]]
df_moedas = df_acoes.astype({"Valor": float})

df_acoes.head(num_linhas_moedas)




#Criando planilha
'''wb = openpyxl.Workbook()
planilha = wb.active
planilha["A1"] = "Ações"
planilha.merged_cells("A1:B1")
planilha["C1"] = "Moedas"
planilha.merged_cells("C1:D1")'''



