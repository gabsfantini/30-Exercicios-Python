def sao_anagramas(string1, string2):
    return sorted(string1) == sorted(string2)

string1 = "amor"
string2 = "roma"
print("São anagramas:", sao_anagramas(string1, string2))
