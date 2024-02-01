def decifrar_cifra_cesar(cifrado, deslocamento):
    decifrado = ""
    for char in cifrado:
        if char.isalpha():
            deslocamento = deslocamento % 26
            codigo = ord(char) - deslocamento
            if char.islower():
                if codigo < ord('a'):
                    codigo += 26
            elif char.isupper():
                if codigo < ord('A'):
                    codigo += 26
            decifrado += chr(codigo)
        else:
            decifrado += char
    return decifrado

# Exemplo de uso
texto_cifrado = "Bqqmft bsf gvo!"
deslocamento = 1
texto_decifrado = decifrar_cifra_cesar(texto_cifrado, deslocamento)
print(texto_decifrado)
