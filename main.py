# adicionar tarefa, revover tarefa, exibir tarefa e armazenar em lista

'''tarefas = []

def adicionar_tarefa(tarefa):
    tarefas.append(tarefa)

def remover_tarefa(tarefa):
    if tarefa in tarefas:
        tarefas.remove(tarefa)


    else:
        print("tarefa não encontrada")

def exibir_tarefa():
    for i, tarefa in enumerate(tarefas, 1):
        print(f"{i}. {tarefa}")


while True:

    menu = int(input("1. Adicionar | 2. remover | 3. exibir | 0 .sair \n"))

    if menu == 0:
        print("programa encerrado")
        break
    
    elif menu == 1:
        tarefa = input("digite uma tarefa a ser adicionada: ").lower().strip()
        adicionar_tarefa(tarefa)
    elif menu == 2:
        remover_tarefa(tarefas)
        tarefa = input("digite uma tarefa a ser removida: ").lower().strip()
    
    elif menu == 3:
        exibir_tarefa()
    else:
        print("valor invalido")'''








while True:
    menu = int(input("1. soma | 2. subtração | 3. multiplicação | 4. divisão | 5. sair  \n"))
    if menu == 5:
        print("programa encerrado")
        break
    elif menu == 1:
        print("SOMA")
        num1 = int(input("digite o primeiro número  "))
        num2 = int(input("digite o psegundo número  "))
        resultado  = (num1 + num2)
        print (f"\n{num1} + {num2} = {resultado}\n")
    elif menu == 2:
        print("SUBTRAÇÃO")

        num1 = int(input("digite o primeiro número  "))
        num2 = int(input("digite o psegundo número  "))
        resultado  = (num1 - num2)
        print (f"\n{num1} - {num2} = {resultado}\n")
    elif menu == 3:
        print("MULTIPLICAÇÃO")

        num1 = int(input("digite o primeiro número  "))
        num2 = int(input("digite o psegundo número  "))
        resultado  = (num1 * num2)
        print (f"\n{num1} * {num2} = {resultado}\n")
    elif menu == 4:

        print("DIVISÃO")
        num1 = int(input("digite o primeiro número  "))
        num2 = int(input("digite o psegundo número  "))
        resultado  = (num1 / num2)
        print (f"\n{num1} / {num2} = {resultado}\n")
    else:
        print("valor invalido")