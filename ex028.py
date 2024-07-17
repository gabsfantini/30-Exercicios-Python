import re

def validar_senha(senha):
    if len(senha) < 8:
        return "Senha muito curta"
    if not re.search("[a-z]", senha):
        return "Senha deve conter letras minúsculas"
    if not re.search("[A-Z]", senha):
        return "Senha deve conter letras maiúsculas"
    if not re.search("[0-9]", senha):
        return "Senha deve conter números"
    if not re.search("[@#$%^&+=]", senha):
        return "Senha deve conter caracteres especiais"
    return "Senha válida"

senha = "Senha@123"
print(validar_senha(senha))
