def criarqrcode(valor, numcarteira):

    # utilizarei a funcção com 2 parametros para formatar o nome do output

    import qrcode
    carteira = (f"O valor da sua carteira é de $ {round(float(valor), 2)} Reais")

    # refinei o texto que será exibido no qrcode

    imagem = qrcode.make(carteira)
    imagem.save(f'Qrcode{numcarteira}.png')

    # aqui a imagem será salva na pasta do projeto

# exemplos de testes, saída: boa
# criarqrcode(23/7, 3)