from bs4 import BeautifulSoup #Biblioteca para achar tags html, depois vamos colocar num dataframe do pandas
import pandas as pd #Biblioteca para guardar data frame
import requests #Biblioteca para extrair uma URL

#WebScraping
#Url do html
url = "https://atronee.github.io/A2-IC-Python/"
# Obtendo o conteúdo da página em formato de texto

data = requests.get(url).text
soup = BeautifulSoup(data,"html.parser")

#Procurando divs com classes:
div_moeda = soup.find("div", class_ = "moeda")

# Procurando as tabelas por classe na página
table_class_moeda = div_moeda.find("table") # tabela de moeda

# Definindo dataframe
#aqui por enquanto só definimos as colunas
df_moeda = pd.DataFrame(columns=["Moeda", "Quantidade por tipo"]) #dataframe da tabela moeda

#Contando o número de linhas em cada tabela
linhas_na_tabela_moeda = [] #Aqui vamos por um item para linha da tabela com dados, para conseguir o número de linhas
for row in table_class_moeda.find_all("tr"):# em html uma linha da tabela é representada pela tag <tr>
    columns_moeda = row.find_all("td") # em html uma coluna da tabela é representada pela tag <td>
    if (columns_moeda != []):
        linhas_na_tabela_moeda.append("linha")
num_linhas_moeda = len(linhas_na_tabela_moeda) #número de linhas em tabela ações
#Obtendo todas as linhas da tabela
        #Obtendo todas as linhas da tabela acoes

for row in table_class_moeda.find_all("tr"): # em html uma linha da tabela é representada pela tag <tr>
    # Obtendo todas as colunas em cada linha
    columns_moeda = row.find_all("td")  # em html uma coluna da tabela é representada pela tag <td>

    if (columns_moeda != []):
        moeda = columns_moeda[0].text.strip(" ")
        quantidade_por_tipo = columns_moeda[1].text.strip(" ")
        df_moeda = pd.concat([df_moeda, pd.DataFrame.from_records([{"Moeda": moeda, "Quantidade por tipo": quantidade_por_tipo}])], ignore_index=True)
        # Aqui a primeira linha vai conter o nosso primeiro df_acoes definido que contém Moeda, Quantidade por tipo, ou seja os nomes das nossas colunas
        # a segunda parte dos nossos dados serão achados pelo método pandas.DataFrame.from_records
        # nele teremos uma lista é claro, pois em cada linha temos mais de uma informação
        # nesta lista queremos a moeda e a quantidade_por_tipo o que a gente tem!
        # pois definimos moeda e quantidade_por_tipo
        # Podemos usar o método com dicionário! a chave do dic é a coluna e o valor é o que a coluna vai receber, no caso moeda e quantidade_por_tipo IZI
        # o ignore_index é para enumerar nossas linhas, note que ele não coloca numero em moeda e quantidade por tipo, pois definimos esse dado como coluna

df_moeda.head(num_linhas_moeda) #Para retornar as num_linhas_acoes desejadas

# Refatorando o dataframe
#Aqui só vou arrumar os dados para ficar da forma certa, pois tratamos eles como str, mas não necessariamente são str
    #Ações
        # Ação
df_moeda["Moeda"] = df_moeda["Moeda"].str.upper()
        # Quantidade
df_moeda["Quantidade por tipo"] = [x.replace(',', '.') for x in df_moeda["Quantidade por tipo"]]
df_moeda = df_moeda.astype({"Quantidade por tipo": float})

df_moeda.head(num_linhas_moeda)

#print(df_moeda.head(num_linhas_moeda))

print(df_moeda["Moeda"])
print(type(df_moeda["Moeda"]))
print(df_moeda["Moeda"][0])
for item in df_moeda["Moeda"]:
    print(item)