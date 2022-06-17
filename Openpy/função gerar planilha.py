import openpyxl
#Preciso por duas entradas na função, uma com o dataframe da moeda e outra com data frame da ação
def gerar_planilha_carteira(df_acoes, df_moedas):
    # Criando planilha
    # Criando folha da carteira
    wb = openpyxl.Workbook()
    sheet_1 = wb.active
    sheet_1.title = "Carteira"
    # tabela de ações
    sheet_1["A1"] = "Ações"
    sheet_1.merge_cells("A1:B1")
    sheet_1["A2"] = "Ação"
    sheet_1["B2"] = "Quantidade"
    # inserindo dados na coluna ações
    cont_acoes = 3
    for nome_acao in df_acoes["Ação"]:
        sheet_1[f"A{cont_acoes}"] = f"{nome_acao}"
        cont_acoes += 1
    # inserindo dados na coluna quantidade
    cont_quant = 3
    for quant_acao in df_acoes["Quantidade"]:
        sheet_1[f"B{cont_quant}"] = f"{quant_acao}"
        cont_quant += 1

    # tabela de moedas
    sheet_1["C1"] = "Moedas"
    sheet_1.merge_cells("C1:F1")
    sheet_1["C2"] = "Moeda"
    sheet_1["D2"] = "Quantidade por tipo"
    sheet_1["E2"] = "Cotação"
    sheet_1["F2"] = "Valor"
    # inserindo dados na coluna ações
    cont_moeda = 3
    for nome_moeda in df_moedas["Moeda"]:
        sheet_1[f"C{cont_moeda}"] = f"{nome_moeda}"
        cont_moeda += 1
    # inserindo dados na coluna quantidade
    cont_quant_tipo = 3
    for quant_moeda in df_moedas["Quantidade por tipo"]:
        sheet_1[f"D{cont_quant_tipo}"] = f"{quant_moeda}"
        sheet_1[f"E{cont_quant_tipo}"] = f"{1}"
        sheet_1[f"F{cont_quant_tipo}"] = f"{3}"
        cont_quant_tipo += 1
    # Salvando planilha
    planilha = wb.save("planilha_carteira.xlsx")
    return planilha

