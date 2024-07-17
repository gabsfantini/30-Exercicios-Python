def calculadora(a, b, operacao):
    if operacao == 'soma':
        return a + b
    elif operacao == 'subtracao':
        return a - b
    elif operacao == 'multiplicacao':
        return a * b
    elif operacao == 'divisao':
        return a / b
    else:
        return "Operação inválida"

print(calculadora(10, 5, 'soma'))
print(calculadora(10, 5, 'subtracao'))
print(calculadora(10, 5, 'multiplicacao'))
print(calculadora(10, 5, 'divisao'))
