alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
mensagem_criptografada = "10JK HC10450C4S050CK9JE02E1"
chave = 3  # Substitua por qualquer chave que você deseja usar

def encontrar_indice(letra, alfabeto):
    if letra in alfabeto:
        return alfabeto.index(letra)
    return -1

def decodificar_com_chave(mensagem, chave, alfabeto):
    mensagem_decodificada = []
    n = len(alfabeto)
    
    for letra in mensagem:
        g = encontrar_indice(letra, alfabeto)
        if g != -1:
            nova_letra = alfabeto[(g - chave) % n]
        else:
            nova_letra = letra
        mensagem_decodificada.append(nova_letra)
    
    return "".join(mensagem_decodificada)

mensagem_decodificada = decodificar_com_chave(mensagem_criptografada, chave, alfabeto)
print(f"Mensagem decriptografada com chave {chave}: {mensagem_decodificada}")
