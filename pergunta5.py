def inverter_string(s):
    
    string_invertida = ""
    
    for caractere in s:
        
        string_invertida = caractere + string_invertida
    
    return string_invertida

s = input("Informe a string a ser invertida: ")

resultado = inverter_string(s)

print(f'String invertida: {resultado}')
