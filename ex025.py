def caixa_eletronico(valor):
    notas = [100, 50, 20, 10, 5, 2, 1]
    for nota in notas:
        if valor >= nota:
            quantidade = valor // nota
            valor = valor % nota
            print(f"{quantidade} nota(s) de R${nota}")

valor = 287
caixa_eletronico(valor)
