lista_de_tarefas = {}

def criar_chave_valor(dia,tarefa,prioridade,categoria):
 if dia in lista_de_tarefas:
        lista_de_tarefas[dia].append((prioridade,tarefa,categoria))
 else:
        lista_de_tarefas[dia] = [(prioridade,tarefa,categoria)]
 print(f"tarefa {tarefa} adicionada para o dia de {dia} na categoria {categoria}")

#=============================================================================



while True:
    print("\ndigite o dia da semana ou sair para encerrar\n")
    dia = input("dia:  ").capitalize()

    if dia.lower() == "sair":
        print("programa encerrado")
        break
    
    tarefa = input(f"tarefa de {dia}:  ")
    prioridade = int(input(f"qual a prioridade das tarefas do dia {dia} digite 1.Alta |2.média |3.Baixa\n  "))
    categoria = input(f"qual a categoria da tarefa {tarefa}  ")
    criar_chave_valor(dia,tarefa,prioridade,categoria)


print("\nAtividades da semana:")

for i,(dia, tarefas) in enumerate(lista_de_tarefas.items(),start=1):
    tarefas_ordenadas = sorted(tarefas,key=lambda x: x[0])
    print(f"{i}.{dia}:")
    for prioridade,tarefa,categoria in tarefas_ordenadas:
        print(f"      -({prioridade}) {tarefa} - categoria:({categoria})")