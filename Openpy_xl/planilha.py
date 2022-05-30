import openpyxl
from bs4 import BeautifulSoup #Biblioteca para achar tags html, depois vamos colocar num dataframe do pandas
import numpy as np
import pandas as pd #Biblioteca para guardar data frame
import requests #Biblioteca para extrair uma URL
import matplotlib.pyplot as plt


#WebScraping
#Url do html
url = "https...."
# Obtendo o conteúdo da página em formato de texto

data = requests.get(url).txt
soup = BeautifulSoup(data,"html.parser")

# Procurando as tabelas por classe na página
table_class_acoes = soup.find("table", class_ = "acoes") # tabela de ações
table_class_moedas = soup.find("table", class_ = "moedas") # tabela de moedas

# Definindo dataframe
df_acoes = pd.DataFrame(columns=["Ações"]) #dataframe da tabela ações
df_moedas = pd.DataFrame(columns=["Moedas"]) #dataframe da tabela moedas
    #Contando o número de linhas em cada tabela
num_linhas_acoes = len(table_class_acoes.tbody.find_all("tr")) #número de linhas em tabela ações
num_linhas_moedas = len(table_class_moedas.tbody.fin_all("tr")) #némero de linhas em tabela moedas
#Obtendo todas as linhas da tabela
for row in table_class_acoes.tbody.find_all("tr"):
    # Obtendo todas as linhas da tabela acoes
for row in table_class_acoes.tbody.find_all("tr"):  # em html uma linha da tabela é representada pela tag <tr>
    # Obtendo todas as colunas em cada linha
    columns = row.find_all("td")  # em html uma coluna da tabela é representada pela tag <td>
    if (columns != []):
        acoes = columns[0].text.strip(" ")
        moedas = columns[1].text.strip(" ")
        df = pd.concat([df, pd.DataFrame.from_records([{"Ações": acoes, "Moedas": moedas}])], ignore_index=True)

df.head(num_linhas_acoes)
#Criando planilha
wb = openpyxl.Workbook()
planilha = wb.active
planilha["A1"] = "Ações"
planilha.merged_cells("A1:B1")
planilha["C1"] = "Moedas"
planilha.merged_cells("C1:D1")



