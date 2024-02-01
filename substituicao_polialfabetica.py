def cifrar_vigenere(texto, chave):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chave = chave.upper()
    texto_cifrado = ''
    chave_index = 0

    for char in texto.upper():
        if char in alfabeto:
            index = (alfabeto.find(char) + alfabeto.find(chave[chave_index])) % len(alfabeto)
            texto_cifrado += alfabeto[index]
            chave_index = (chave_index + 1) % len(chave)
        else:
            texto_cifrado += char
    
    return texto_cifrado

def decifrar_vigenere(texto_cifrado, chave):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chave = chave.upper()
    texto_decifrado = ''
    chave_index = 0

    for char in texto_cifrado.upper():
        if char in alfabeto:
            index = (alfabeto.find(char) - alfabeto.find(chave[chave_index])) % len(alfabeto)
            texto_decifrado += alfabeto[index]
            chave_index = (chave_index + 1) % len(chave)
        else:
            texto_decifrado += char
            
    return texto_decifrado

#Testando as funções
texto = "ATAQUEAMANHA"
chave = "LIMAO"

texto_cifrado = cifrar_vigenere(texto, chave)
print("Texto Cifrado: ", texto_cifrado)

texto_decifrado = decifrar_vigenere(texto_cifrado, chave)
print("Texto Decifrado: ", texto_decifrado)