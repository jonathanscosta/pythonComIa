#Crie um conjunto vazio chamado frutas e adicione as seguintes frutas a ele:"maçã","banana","uva",
# "laranja"e"morango. Em seguida, imprima o conjunto.

'''frutas = set()
frutas.update (["maça", "banana", "uva", "laranja", "morango"])
print(frutas)'''

# fiz uma variação do exercicio acima deixando ele mais completo, permitindo uma interação com usuário
# usei um laço while para que o usuário podesse adicionar quantos itens quisesse na lista encerrando com fim
# depois um laço for para que imprimisse a em formato de lista com um item em cima do outro

'''frutas = set()
while True:
  adicionar = input("adicione sua lista de compras ou digite fim para encerrar  ")
  if adicionar == "fim":
    break
  else:
     frutas.add(adicionar)
for x in frutas:


 print(x)'''
 

#Verifique se a fruta"banana" está presente no conjunto frutas e imprima o resultado.

'''frutas = {"banana","maça","uva"}
print("banana" in frutas)'''

#criar um conjunto chamado frutas_vermelhas e adicionar frutas depois imprimir o conjunto

'''frutas_vermelhas = set()
frutas_vermelhas.update(["morango","cereja","framboesa"])
print(f"frutas vermelhas {frutas_vermelhas}")'''

#remover a fruta cereja e imprimir o conjunto atualizado

'''frutas_vermelhas.remove("cereja")
print(f"frutas vermelhas atualizadas {frutas_vermelhas}")'''

#criar dois conjuntos a e b e fazer a união deles

'''conjuntoA = {1,3,5,7,9}
conjuntoB = {2,4,6,8,10}
print(conjuntoA.union(conjuntoB))'''
#criar um porgrama que receba dois conjuntos e crie a interseção entre eles

'''conjuntoA = {1,2,3,4}
conjuntoB = {3,4,5,6}
print(conjuntoA.intersection(conjuntoB))'''

#Escreva um programa que receba duas listas e calcule,a união dos elementos únicos dessas listas, 
# usando conjuntos.

'''lista1 = [1,2,3,4,5]
lista2 = [4,5,6,7]
conjunto = set(lista1)
conjunto2 = set(lista2)
uniao = conjunto.union(conjunto2)
print(uniao)'''

#dicionários

#crie um dicionário com informações de nome e idade e depois exiba

'''dados_do_usuario = {"nome":"jonathan","idade":38,"cidade":"fortaleza"}
print(dados_do_usuario)'''

#fiz uma variação do exercicio anterior com interação do usuário

'''dados_do_usuario = {"nome":"jonathan","idade":38,"cidade":"fortaleza"}
usuario = int(input("para saber o nome digite [1], para idade digite[2] para cidade digite[3]  "))

if usuario == 1:
  print(f"seu nome é:{dados_do_usuario ['nome']}")
elif usuario == 2:
  print(f"sua idade é:{dados_do_usuario ['idade']}")
else:
  print(f"sua cidade é:{dados_do_usuario ['cidade']}")'''

#Escreva um programa que percorra as chaves e valores de um dicionário separadamente e os exiba.

'''dados_do_usuario = {"nome":"jonathan","idade":38,"cidade":"fortaleza"}

for chave,valor in dados_do_usuario.items():

 print(f"{chave}: {valor}")'''

 # Desenvolva um programa que recebe um dicionário, uma chave e um valor como entrada e adiciona a chave e o
 # valor ao dicionário, atualizando o valor se a chave já existir.

'''dados_do_usuario = {"nome":"jonathan","idade":38}
novaChave = input("digite uma nova chave  ")
novoValor = input("digite o novo valor  ")
dados_do_usuario [novaChave] = novoValor
print(dados_do_usuario)'''

# Escreva um programa que recebe um dicionário e uma lista de chaves como entrada e verifica se todas as
# chaves da lista existem no dicionário. A função deve retornar True se todas as chaves existirem e False caso
# contrário.
# descobri essa função all e a função any que ajudam muito

'''dicionario = {"nome":"jonathan","idade":38, "cidade":"fortaleza"}
lista = ["nome","idade","cidade","bairro"]
todas_presentes = all (chave in dicionario for chave in lista)

print(todas_presentes)'''

# fiz uma pequena atualização no programa anterior

'''dicionario = {"nome":"jonathan","idade":38, "cidade":"fortaleza"}
lista = ["nome","idade","cidade"]
todas_presentes = all (chave in dicionario for chave in lista)
if todas_presentes == True:
 print("todas as chaves na lista estão no dicionário")
else:
  print("nem todas as chaves da lista estão no dicionário")'''

# Crie um programa que simule um sistema de votação.
# programa deve permitir que os eleitores escolham entre
# opções de eleitores e conte os votos para cada opção.
# Use um dicionário para armazenar os resultados da
# votação, onde as chaves são as opções e os valores são o
# número de votos para cada opção. O programa deve
# permitir que os eleitores votem, encerre a votação e exiba
# os resultados finais. Use While True e pare o programa
# somente se o usuário digitar o número 0 e exiba os resultados finais.

'''candidatos = ["lula","bolsonaro"]
votacao = dict.fromkeys(candidatos,0)

while True:
  voto = int(input("digite 13 para lula ou 17 para bolsonaro e 0 para encerrar:  "))

  if voto == 0:
    break
  elif voto == 13:
    votacao["lula"] += 1
  elif voto == 17:
    votacao["bolsonaro"] += 1
  else:
    print("valor invalido")

print(votacao)'''

# fiz uma pequena alteração no código, agora independente de quantos votos bolsonaro receba lula sempre ganha 
# simulando as urnas de verdade kkkkk

'''candidatos = ["lula","bolsonaro"]
votacao = dict.fromkeys(candidatos,0)

while True:
  voto = int(input("digite 13 para lula ou 17 para bolsonaro e 0 para encerrar:  "))

  if voto == 0:
    break
  elif voto == 13:
    votacao["lula"] += 1
  elif voto == 17:
    votacao["bolsonaro"] += 1
  else:
    print("valor invalido")
if votacao["bolsonaro"] > votacao["lula"]:
  votacao["lula"] = votacao["bolsonaro"] +1

print(votacao)'''

# Crie um dicionário que relacione nomes de alunos às suas
# notas em uma disciplina. Calcule a média das notas e exiba-a.

'''alunos = {"joão":[10,8,9],"pedro":[8,10,7],"enzo":[5,9,6],}

medias = []

for aluno, notas in alunos.items():
    media = sum(notas)/len(notas)
    medias.append((aluno,media))
    print(f"a nota do trimestre do aluno {aluno} são: {notas}")


ranking = sorted(medias, key=lambda x:x[1], reverse=True)
print("\nranking dos alunos")
for posicao,(aluno,media) in enumerate(ranking,start=1):

 

  print(f"{posicao}º lugar aluno: {aluno} média:{media:.2f}")'''

# Crie um programa que receba uma lista de números e
# remova todas as duplicatas usando um conjunto (set). Em
# seguida, exiba a lista original e a lista sem duplicatas.

'''numeros = [1,2,2,3,3,4,5,6,7]
numeros_unicos = set(numeros)
print(numeros_unicos)'''

# Crie um programa que realize a união de múltiplos
# conjuntos e exiba o conjunto resultante.

'''numeros1 = {1,3,5,7,9}
numeros2 = {2,4,6,8,10}
uniao = numeros1.union(numeros2)
print(uniao)'''

# desafio prático: cadastro de alunos

cadastro_de_alunos = []

# Loop para cadastrar 3 alunos
for i in range(2):
    print(f"\nCadastro do aluno {i + 1}:")
    
    # Criar um dicionário para o aluno atual
    aluno = {"nome": None, "idade": None, "notas": {"matemática": [], "ciências": [], "história": []}, "media": 0}
    
    # Preencher nome e idade
    aluno["nome"] = input("Digite o nome do aluno: ")
    aluno["idade"] = int(input("Digite a idade do aluno: "))
    
    # Preencher as notas para cada matéria
    for materia in aluno["notas"]:
        print(f"\nDigite 3 notas para {materia}:")
        for j in range(3):
            nota = float(input(f"Digite a nota {j + 1} para {materia}: "))
            aluno["notas"][materia].append(nota)
    
    # Calcular a média geral das notas do aluno
    soma_total = 0
    total_notas = 0
    for notas in aluno["notas"].values():
        soma_total += sum(notas)
        total_notas += len(notas)
    aluno["media"] = soma_total / total_notas
    
    # Adicionar o aluno ao cadastro
    cadastro_de_alunos.append(aluno)

# Identificar o aluno com a melhor média
melhor_aluno = max(cadastro_de_alunos, key=lambda x: x["media"])

# Exibir os cadastros
print("\nCadastro finalizado:")
for aluno in cadastro_de_alunos:
    print(f"\nNome: {aluno['nome']}, Idade: {aluno['idade']}, Média: {aluno['media']:.2f}")
    for materia, notas in aluno["notas"].items():
        print(f"  {materia.capitalize()}: {notas}")

# Exibir o aluno com a melhor média
print("\nAluno com a melhor média:")
print(f"Nome: {melhor_aluno['nome']}, Média: {melhor_aluno['media']:.2f}")

