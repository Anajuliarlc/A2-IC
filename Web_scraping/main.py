from biblioteca import Funcoes #importando funções
url_carteira = input("Digite a url da sua carteira: ") #input digite sua url
url_carteira = url_carteira.strip() #tratando o input
Funcoes.gerar_planilha_carteira(url_carteira)
#Digite a url da sua carteira e abra o arquivo planilha_carteira.xlsx
