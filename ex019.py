string = "Olá, Mundo!"
vogais = "aeiouAEIOU"
contagem = sum(1 for char in string if char in vogais)
print("Número de vogais:", contagem)

