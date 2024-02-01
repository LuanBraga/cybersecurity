import random

def gerar_chave_publica(chave_privada, multiplicador, modulo):
    return [x * multiplicador % modulo for x in chave_privada]

def cifrar_mensagem(mensagem, chave_publica):
    return sum(chave_publica[i] for i in range(len(mensagem)) if mensagem[i] == '1')

def decifrar_mensagem(mensagem_cifrada, chave_privada, multiplicador, modulo):
    # Invertendo a multiplicação e o módulo
    mensagem_cifrada = mensagem_cifrada * pow(multiplicador, -1, modulo) % modulo

    # Resolvendo a mochila supercrescente
    mensagem_original = ''
    for peso in reversed(chave_privada):
        if mensagem_cifrada >= peso:
            mensagem_cifrada -= peso
            mensagem_original = '1' + mensagem_original
        else:
            mensagem_original = '0' + mensagem_original

    return mensagem_original

# Exemplo de uso
chave_privada = [1, 2, 4, 8, 16, 32]
modulo = 101  # Escolhendo um número primo como módulo
multiplicador = random.randint(2, 100)  # O multiplicador deve ser menor que o módulo

chave_publica = gerar_chave_publica(chave_privada, multiplicador, modulo)
mensagem = '101010'
mensagem_cifrada = cifrar_mensagem(mensagem, chave_publica)

mensagem_decifrada = decifrar_mensagem(mensagem_cifrada, chave_privada, multiplicador, modulo)

print("Chave Privada:", chave_privada)
print("Chave Pública:", chave_publica)
print("Mensagem Cifrada:", mensagem_cifrada)
print("Mensagem Decifrada:", mensagem_decifrada)