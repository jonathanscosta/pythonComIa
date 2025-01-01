#lista de números de 1 a 5 e depois exibir com print()
'''numeros = [1,2,3,4,5]
print(numeros)'''
# lista de vogais depois exibir lista com print()
'''vogais = ['a','e','i','o','u']
print(vogais)'''
# lista com 5 itens em que 3 são de classes diferentes depois exibir o terceiro item da lista
'''lista = ['maça', 10.0,True,10,"jonathan"]
print(lista[2])'''

#quis brincar criando uma lista de comprar limitada por uma quantidade de itens a ser acrescentado que exiba 
# a lista com cochetes na frente permitindo marcar com o "x" quando impresso
'''lista = []
tentativas = 3

while tentativas >0:
    anotar = input("")
    lista.append(anotar)
    tentativas -= 1
for item in lista:
     
 print(f"[]",item)'''

#brincando com a tupla
'''frutas = ("maça","banana","banana","laranja")
indice_laranja = frutas.index("laranja")
print(f"o indice da laranja é: {indice_laranja}")
quantidadeDeBananas = frutas.count("banana")
print(f"a quantidade de bananas é {quantidadeDeBananas}")'''
#criar uma tupla em que contenha as informações de 3 palestrantes com nome, palestra e instituição
# depois exibir o 3º palestrante
#modifiquei para que o usuário possa escolher a palestra digitando um número,corrigi um pequeno erro
# quando o usuário digita um número que não seja de 1 a 3, criei uma laço de repetição com uma mensagem
# de erro para usuário digitar novamente até escolher um dos números corretos, depois exibe na tela
# o palestrante com o nome de sua palestra e a instituição de origem(fiz tudo sem consultar qualquer IA XD)
'''convidado = ("lula","pablo marçal","fátima bernardes")
palestra = ("como afundar o país em 4 anos",
            "como enganar tanto otário ao mesmo tempo",
            "como destruir a infância de uma geração")
instituição = ("prisão da papuda", "colt de internet","globo")
usuario = int(input("qual palestra deseja assistir? palestra 1,2 ou 3  "))
while usuario <=0 or usuario >3:
     print("digite um número de 1 à 3")
     usuario = int(input("qual palestra deseja assistir? palestra 1,2 ou 3  "))
     
else:

 if usuario == 1:
    print(f"palestra com {convidado[0]} sobre:{palestra[0]}, que veio da instituição: {instituição[0]}")
 elif usuario == 2:
     print(f"palestra com {convidado[1]} sobre:{palestra[1]}, que veio da instituição: {instituição[1]}")
 else:
      print(f"palestra com {convidado[2]} sobre:{palestra[2]}, que veio da instituição: {instituição[2]}")'''

# criar uma lista de tuplas para uma competição, cada tupla tem o nome da equipe e uma lista de pontos,
# calcular a media de pontos de cada equipe e armazenar em uma nova lista chamada média
# ordenar as medias em ordem decrescente
# criar uma nova lista em que tenha o nome da equipe e sua média
# exibir na tela a classificação do mais alto para o mais baixo
# aqui usei algumas funções que aprendi como sorted, enumerate e reverse = True

resultado = [('equipe 1',[10,20,50]),('equipe 2',[15,22,45]),('equipe 3',[10,25,50]),]
media = [(nome,sum (pontos) / len(pontos)) for nome,pontos in resultado]

media_ordenada = sorted (media,key = lambda x: x[1],reverse=True)

print("pontuação final")
for i,(nome, media) in enumerate (media_ordenada, start = 1):
   
    print(f"{i}º lugar {nome} - media: {media:.2f}")

