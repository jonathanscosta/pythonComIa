import json

def criar_arquivo_json():
    usuarios = [
        {"nome": "João", "idade": 25, "endereco": "Rua A, 123"},
        {"nome": "Maria", "idade": 30, "endereco": "Avenida B, 456"}
    ]
    with open("usuarios.json", "w") as arquivo:
        json.dump(usuarios, arquivo, indent=4)
    print("Arquivo JSON criado com sucesso!")

def adicionar_usuario():
    try:
        with open("usuarios.json", "r") as arquivo:
            usuarios = json.load(arquivo)
        
        nome = input("Digite o nome do usuário: ")
        idade = int(input("Digite a idade do usuário: "))
        endereco = input("Digite o endereço do usuário: ")
        novo_usuario = {"nome": nome, "idade": idade, "endereco": endereco}

        usuarios.append(novo_usuario)

        with open("usuarios.json", "w") as arquivo:
            json.dump(usuarios, arquivo, indent=4)
        print("Usuário adicionado com sucesso!")
    except FileNotFoundError:
        print("Arquivo não encontrado. Crie o arquivo primeiro.")
    except ValueError:
        print("Por favor, insira uma idade válida.")

def exibir_usuarios():
    try:
        with open("usuarios.json", "r") as arquivo:
            usuarios = json.load(arquivo)

        if not usuarios:  # Se não houver usuários no arquivo
            print("Nenhum usuário registrado.")
        else:
            print("Usuários registrados:")
            for usuario in usuarios:
                print(f"Nome: {usuario['nome']}, Idade: {usuario['idade']}, Endereço: {usuario['endereco']}")
    except FileNotFoundError:
        print("Arquivo não encontrado. Crie o arquivo primeiro.")
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo. O arquivo pode estar vazio ou corrompido.")

def excluir_usuario():
    try:
        with open("usuarios.json", "r") as arquivo:
            usuarios = json.load(arquivo)

        nome_excluir = input("Digite o nome do usuário a ser excluído: ")

        usuario_encontrado = False
        for usuario in usuarios:
            if usuario['nome'].lower() == nome_excluir.lower():
                usuarios.remove(usuario)
                usuario_encontrado = True
                print(f"Usuário {nome_excluir} excluído com sucesso!")
                break

        if not usuario_encontrado:
            print(f"Usuário {nome_excluir} não encontrado.")

        with open("usuarios.json", "w") as arquivo:
            json.dump(usuarios, arquivo, indent=4)

    except FileNotFoundError:
        print("Arquivo não encontrado. Crie o arquivo primeiro.")

def atualizar_usuario():
    try:
        with open("usuarios.json", "r") as arquivo:
            usuarios = json.load(arquivo)

        nome_atualizar = input("Digite o nome do usuário a ser atualizado: ")

        usuario_encontrado = False
        for usuario in usuarios:
            if usuario['nome'].lower() == nome_atualizar.lower():
                usuario_encontrado = True
                print(f"Usuário encontrado: {usuario['nome']}, Idade: {usuario['idade']}, Endereço: {usuario['endereco']}")

                idade_nova = int(input("Digite a nova idade: "))
                endereco_novo = input("Digite o novo endereço: ")

                usuario['idade'] = idade_nova
                usuario['endereco'] = endereco_novo
                print(f"Usuário {nome_atualizar} atualizado com sucesso!")

                break

        if not usuario_encontrado:
            print(f"Usuário {nome_atualizar} não encontrado.")

        with open("usuarios.json", "w") as arquivo:
            json.dump(usuarios, arquivo, indent=4)

    except FileNotFoundError:
        print("Arquivo não encontrado. Crie o arquivo primeiro.")
    except ValueError:
        print("Por favor, insira uma idade válida.")

# Menu principal
print("Bem-vindo ao Gerenciador de Usuários JSON!")
while True:
    print("\nEscolha uma opção:")
    print("1. Criar arquivo JSON")
    print("2. Adicionar usuário")
    print("3. Exibir usuários")
    print("4. Excluir usuário")
    print("5. Atualizar usuário")
    print("6. Sair")

    opcao = input("Digite sua escolha: ")

    if opcao == "1":
        criar_arquivo_json()
    elif opcao == "2":
        adicionar_usuario()
    elif opcao == "3":
        exibir_usuarios()
    elif opcao == "4":
        excluir_usuario()
    elif opcao == "5":
        atualizar_usuario()
    elif opcao == "6":
        print("Saindo... Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
