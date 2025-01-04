cadastro_de_clientes = []

while True:
    cliente = {"nome":None,"telefone":None,"E-mail":None}
    
    for cadastro in cliente.keys():
     dados = str(input(f"\ndigite o {cadastro} do cliente ou sair para sair do programa  "))
     
     if dados.lower().strip() == "sair":
        print("programa encerrado")
        exit()
     else:
        cliente[cadastro] = dados
       
    print(f"\ndados do cliente \n\nnome do cliente: {cliente["nome"]}, \ntefefone do cleinte: {cliente["telefone"]},\nE-mail do cliente: {cliente["E-mail"]}")
   


