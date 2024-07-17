def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = 70  # em kg
altura = 1.75  # em metros
imc = calcular_imc(peso, altura)
print("Seu IMC é:", imc)
