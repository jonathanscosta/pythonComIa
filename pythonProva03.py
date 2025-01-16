
# Crie um dicionário para armazenar o nome e o preço de cinco produtos. 
# Peça ao usuário para inserir o nome de cada produto e o respectivo preço. 
# À medida que o usuário fornece os dados, armazene cada produto como uma chave no dicionário e o preço como o valor associado a essa chave. 
# Após a inserção de todos os produtos e preços, calcule o valor total da compra somando todos os preços armazenados no dicionário. 
# Por fim, exiba o valor total da compra.

produtos = {}
for i in range(1,6):

 nome = input(f"digite o nome do {i}º produto:  ")
 valor = float (input(f"digite o valor do {i}º produto:  "))
 produtos[nome] = valor

 valor_total = sum(produtos.values())

print("produtos e preços inseridos:  \n")

for produto, preco in produtos.items():
    print(f"{produto}:  R$ {preco:.2f}")
print(f"\nValor total da compra: R$ {valor_total:.2f}")