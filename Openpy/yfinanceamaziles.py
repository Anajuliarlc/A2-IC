import yfinance as yf


# transforma cada item dos arrays do dicionário de arrays em dicionário
def main(carteiraDicionario):
    # declara um dicionário vazio
    carteiraEntrega = []
    # pega a primeira chave do dicionário
    keys = next(iter(carteiraDicionario.keys()))

    # direciona os itens modificados como dicionário para seu determinado tratamento
    if "Ação" in keys:
        lista_dic_acoes = []
        for acao in carteiraDicionario["Ação"]:
            carteiraTemporario = {
                "Ação": carteiraDicionario["Ação"][0],
                "Quantidade por tipo": float(carteiraDicionario["Ação"][1])
            }
            carteiraEntrega["Ação"] = main2(carteiraTemporario)
        return carteiraEntrega
    elif 'Moeda' in keys:
        for moeda in carteiraDicionario:
            carteiraTemporario = {
                "Moeda": carteiraDicionario[moeda][0],
                "Quantidade por tipo": float(carteiraDicionario[moeda][1])
            }
            carteiraEntrega[moeda] = main2(carteiraTemporario)
        return carteiraEntrega


def main2(carteira):
    # pega as informacoes do primeiro item do dicionario
    keys = next(iter(carteira.items()))

    # acessa a primeira chave do primeiro item, e checa se e acao ou moeda e direciona para a funcao correspondente
    if 'Ação' in keys:
        return calcularTotalAcao(carteira)
    elif 'Moeda' in keys:
        return checarBRL(carteira)


def calcularTotalAcao(carteira):
    ticker = yf.Ticker(carteira['Ação'])

    # checando se a ação existe
    if ticker.info['regularMarketPrice'] == None:
        print(carteira['Ação'], 'Ação nao foi encontrada')
        return
    else:
        # pega a moeda base da acao
        moedaDaAcao = ticker.info['currency']

        # a variavel preco da acao vai ser igual ao preco atual da acao na sua moeda base
        precoDaAcao = ticker.info['regularMarketPrice']

        if moedaDaAcao != "BRL":
            # se a moeda nao for igual a o BRL chamar a funcao converter() para converter para BRL, essa funcao vai retornar o preco de uma acao em BRL então para calcular o valor total das acoes em BRL ce tem q multiplicar a quantidade das acoes pelo preco em brl
            cotacaoDaMoedaEstrangeiro = converter(moedaDaAcao)

            # multiplica o preco de UMA acao na sua moeda estrangeira pela cotacao da da moeda estrangeira em relacao ao BRL
            valorDasAcoesEmBRL = cotacaoDaMoedaEstrangeiro * precoDaAcao

            # multiplica o preco da acao em BRL pela quantidade para calcular o valor total das acoes nessa carteira
            valorTotalDasAcoesNaCarteira = valorDasAcoesEmBRL * carteira['Quantidade por tipo']

            dicionarioFinal = {
                "Ação": carteira['Ação'],
                "Quantidade por tipo": carteira['Quantidade por tipo'],
                "Valor total das ações": valorTotalDasAcoesNaCarteira
            }

            return dicionarioFinal

        else:
            # se a moeda for BRL
            # calcula o valor das acoes multiplicando o valor de uma acao pela quantidade
            valorTotalDasAcoes = carteira['Quantidade por tipo'] * precoDaAcao

            dicionarioFinal = {
                "Ação": carteira['Ação'],
                "Quantidade por tipo": carteira['Quantidade por tipo'],
                "Valor total das ações": valorTotalDasAcoes
            }

            return dicionarioFinal


def converter(moedaEstrangeira):
    # concatena a moeda da acao estrangeiro com a base BRL=X (ex. 'USD'BRL=X) para pegar informacoes da currency
    baseMoeda = moedaEstrangeira + "BRL=X"
    tickerMoeda = yf.Ticker(baseMoeda)

    # pega a cotacao da moeda estrangeira em relacao ao BRL
    precoDaAcaoEmBRL = tickerMoeda.info['regularMarketPrice']

    return precoDaAcaoEmBRL


def atribuirCaracteres(carteira):
    # pega os 3 primeiros caracteres da chave moeda e direciona p funcao converter cambio
    carteira['Moeda'] = carteira['Moeda'][:3]
    return calcularTotalCambio(carteira)


def calcularTotalCambio(carteira):
    # concatena os 3 caracteres da moeda com BRL=X
    moeda = carteira['Moeda'] + "BRL=X"
    tickerMoeda = yf.Ticker(moeda)

    if tickerMoeda.info['regularMarketPrice'] == None:
        print(carteira['Moeda'], 'Moeda não encontrada')
        return

    else:
        precoDaMoedaEmBRL = tickerMoeda.info['regularMarketPrice']

        # multiplica o preço da moeda em real, encontrando o valor total das moedas em real
        valorDasMoedasEmBRL = precoDaMoedaEmBRL * carteira['Quantidade por tipo']

        dicionarioFinal = {
            "Moeda": carteira['Moeda'],
            "Quantidade por tipo": carteira['Quantidade por tipo'],
            "Valor das Moedas": valorDasMoedasEmBRL
        }

        return dicionarioFinal

dic = {'Ação': {'OIBR3.SA': '1702.0', 'MGLU3.SA': '507.0', 'NUBR33.SA': '423.0', 'GME': '9.2'}, 'Moeda': {'JPYBRL=X': '28921.0', 'MXNBRL=X': '473.3', 'ZARBRL=X': '998.09'}}

print(main(dic))