from biblioteca import Funcoes
url_carteira = input("Digite a url da sua carteira: ")
url_carteira = url_carteira.strip()
planilha = Funcoes.gerar_planilha_carteira(url_carteira)


