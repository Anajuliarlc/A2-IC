import qrcode
import openpyxl


def soma_valores(nome_arquivo):

    # Abre a planilha
    planilha = openpyxl.load_workbook(nome_arquivo)
    # Abre a folha Carteira
    carteira = planilha["Carteira"]
    # Pega o tamanho da carteira
    tamanho_tabela = len(list(carteira.rows))
    # Define o valor total da carteira
    soma_total = float()
    for linha in range(3, tamanho_tabela+1):
        soma_total += carteira.cell(row=linha, column=4).value
        soma_total += carteira.cell(row=linha, column=8).value
    # Salva a planilha
    return soma_total


def criarqrcode(nome_arquivo, numcarteira):
    #Puxa a função de cima
    soma_total = soma_valores(nome_arquivo)
    #Insere a mensagem que vai ser lida no qrcode
    carteira = (f"O valor da sua carteira é de R$ {round(soma_total, 2)}")

    #Salva a imagem do qrcode
    imagem = qrcode.make(carteira)
    imagem.save(f'qrcode{numcarteira}.png')

