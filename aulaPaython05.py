def maior_numero(lista):
    maior = sorted(lista,reverse=True)[0]
    return maior



lista_organizada = [7,10,8]

print(maior_numero(lista_organizada))