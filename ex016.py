def busca_binaria(lista, x):
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == x:
            return meio
        elif lista[meio] < x:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1

numeros = [10, 20, 30, 40, 50]
x = 30
print("Elemento encontrado na posição:", busca_binaria(numeros, x))
