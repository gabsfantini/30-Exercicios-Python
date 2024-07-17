def busca_linear(lista, x):
    for i in range(len(lista)):
        if lista[i] == x:
            return i
    return -1

numeros = [10, 20, 30, 40, 50]
x = 30
print("Elemento encontrado na posição:", busca_linear(numeros, x))
