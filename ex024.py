num = 153
n = len(str(num))
soma = sum(int(digito) ** n for digito in str(num))
if num == soma:
    print(num, "é um número Armstrong")
else:
    print(num, "não é um número Armstrong")
