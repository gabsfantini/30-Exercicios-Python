def converter_moeda(valor, taxa):
    return valor * taxa

dolar_para_real = 5.25
valor_em_dolares = 100
valor_em_reais = converter_moeda(valor_em_dolares, dolar_para_real)
print("Valor em reais:", valor_em_reais)
