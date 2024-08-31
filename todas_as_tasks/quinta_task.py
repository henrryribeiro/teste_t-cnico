def inverter_string(s):
    invertida = ""
    for i in range(len(s) - 1, -1, -1):
        invertida += s[i]
    return invertida

# Exemplo de uso
string_para_inverter = input("Digite uma string para inverter: ")
string_invertida = inverter_string(string_para_inverter)
print("String invertida:", string_invertida)

