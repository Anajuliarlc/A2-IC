def criarqrcode(valor, numcarteira):

    # Função que cria Qrcode com o valor total da carteira do cliente

    # utilizarei a função com 2 parâmetros para formatar o nome do output

    import qrcode
    carteira = (f"O valor da sua carteira é de R$ {round(float(valor), 2)}")

    # refinei o texto que será exibido no qrcode

    imagem = qrcode.make(carteira)
    imagem.save(f'../Imagens/Qrcode/Qrcode{numcarteira}.png')

    # aqui a imagem será salva na pasta do projeto
