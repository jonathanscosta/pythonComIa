lista_de_tarefas = {}
dias_da_semana = ["segunda","terça","quarta","quinta","sexta","sábado","domingo","sair"]



def criar_chave_valor(dia,tarefa,prioridade,categoria):
    if dia in lista_de_tarefas:
        lista_de_tarefas[dia].append((prioridade,tarefa,categoria))
    else:
        lista_de_tarefas[dia] = [(prioridade,tarefa,categoria)]
        print(f"A tarefa {tarefa} adicionada no dia de {dia} na categoria {categoria}")



while True:
    print("\ndigite o dia da semana ou sair para encerrar\n")
    
    dia = input("dia: ")
    if dia in dias_da_semana:

     if  dia == "sair":
        print("programa encerrado")
        print(dia)
        break
     else:
        tarefa = input(f"qual a tarefa do dia {dia}  ")
        prioridade = int(input(f"qual a prioridade para a tarefa: {tarefa} 1.Alta | 2.Média | 3.Baixa  "))
        categoria = input(f"qual a categoria da tarefa {tarefa}  ")
        criar_chave_valor(dia,tarefa,prioridade,categoria)
    else:
       print("digite apenas dias da semana")
       input("aperte enter para continuar...")

print("\n tarefas da semana")

for i,(dias,tarefas) in enumerate(lista_de_tarefas.items(),start=1):
    tarefas_ordenadas = sorted(tarefas,key=lambda x: x[0])
    print(f"{i}.{dias}")
    for prioridade,tarefa,categoria in tarefas_ordenadas:
        print(f"   - ({prioridade}) {tarefa} - categoria:({categoria})")
