import random

# Lista fixa de possíveis vouchers
vouchers = [1, 2, 3, 4]

# Lista para armazenar os dados dos convidados
convidados = []

# Conjunto para armazenar os convidados únicos
convidados_unicos = set()

# Exibe o menu inicial
print("1. Adicionar | 2.Visualizar | 3.Atualizar | 4.Excluir | 5. Indicar convidados | 0. Parar")

# Loop principal do programa
while True:
    menu = int(input("Menu: "))

    if menu == 0:  # Opção para encerrar o programa
        print("Programa encerrado")
        break

    elif menu == 1:  # Adicionar um novo convidado
        nome = input("Nome do convidado: ").strip().lower()
        telefone = int(input("Telefone do convidado: "))
        voucher = random.choice(vouchers)

        # Verifica se o nome, telefone ou voucher já existem na lista
        duplicado = any(
            convidado["nome"] == nome or
            convidado["telefone"] == telefone or
            convidado["voucher"] == voucher
            for convidado in convidados
        )

        if duplicado:
            print("Erro: Nome, telefone ou voucher já existe. Convidado não adicionado.")
        else:
            # Adiciona o convidado à lista e ao conjunto de convidados únicos
            convidados.append({"nome": nome, "telefone": telefone, "voucher": voucher, "convidados_indicados": set()})
            convidados_unicos.add(nome)
            print("Convidado adicionado com sucesso!")

    elif menu == 2:  
        if not convidados:
            print("Nenhum convidado foi adicionado ainda.")
        else:
            print("\nLista de convidados:")
            for i, convidado in enumerate(convidados, start=1):
                print(f"{i}. Nome: {convidado['nome']}, Telefone: {convidado['telefone']}, Voucher: {convidado['voucher']}")
                if convidado["convidados_indicados"]:
                    print(f"   Convidados indicados: {', '.join(convidado['convidados_indicados'])}")

    elif menu == 3:  
        if not convidados:
            print("Nenhum convidado para atualizar.")
        else:
            print("\nLista de convidados:")
            for i, convidado in enumerate(convidados, start=1):
                print(f"{i}. Nome: {convidado['nome']}, Telefone: {convidado['telefone']}, Voucher: {convidado['voucher']}")

            escolha = int(input("Digite o número do convidado que deseja atualizar: ")) - 1
            if 0 <= escolha < len(convidados):
                novo_nome = input("Novo nome: ").strip().lower()
                novo_telefone = int(input("Novo telefone: "))
                novo_voucher = random.choice(vouchers)

                duplicado = any(
                    (convidado["nome"] == novo_nome or
                     convidado["telefone"] == novo_telefone or
                     convidado["voucher"] == novo_voucher)
                    and convidado != convidados[escolha]
                    for convidado in convidados
                )

                if duplicado:
                    print("Erro: Nome, telefone ou voucher já existe. Atualização cancelada.")
                else:
                    convidados_unicos.discard(convidados[escolha]["nome"]) 
                    convidados[escolha]["nome"] = novo_nome
                    convidados[escolha]["telefone"] = novo_telefone
                    convidados[escolha]["voucher"] = novo_voucher
                    convidados_unicos.add(novo_nome)  
                    print("Convidado atualizado com sucesso!")
            else:
                print("Opção inválida.")

    elif menu == 4:  
        if not convidados:
            print("Nenhum convidado para excluir.")
        else:
            print("\nLista de convidados:")
            for i, convidado in enumerate(convidados, start=1):
                print(f"{i}. Nome: {convidado['nome']}, Telefone: {convidado['telefone']}, Voucher: {convidado['voucher']}")

            escolha = int(input("Digite o número do convidado que deseja excluir: ")) - 1
            if 0 <= escolha < len(convidados):
                convidados_unicos.discard(convidados[escolha]["nome"])  
                convidados.pop(escolha)  
                print("Convidado excluído com sucesso!")
            else:
                print("Opção inválida.")

    elif menu == 5:  
        if not convidados:
            print("Nenhum convidado disponível para indicar.")
        else:
            print("\nLista de convidados:")
            for i, convidado in enumerate(convidados, start=1):
                print(f"{i}. Nome: {convidado['nome']}")

            escolha = int(input("Digite o número do convidado que irá indicar outros: ")) - 1
            if 0 <= escolha < len(convidados):
                while len(convidados[escolha]["convidados_indicados"]) < 3:
                    indicado = input("Digite o nome do convidado a ser indicado: ").strip().lower()
                    if indicado in convidados_unicos:
                        print("Erro: Este convidado já foi indicado por outra pessoa.")
                    else:
                        convidados[escolha]["convidados_indicados"].add(indicado)
                        convidados_unicos.add(indicado)
                        print(f"{indicado} foi indicado com sucesso!")
            else:
                print("Opção inválida.")
    else:
        print("Opção inválida. Tente novamente.")

