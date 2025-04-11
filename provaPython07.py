import random

def resultado(valor1,valor2):
    soma = valor1 + valor2
    return soma

def lancar_dados(dado):
    jogar = random.choice(dado)
    return jogar

dado01 = [1,2,3,4,5,6]
dado02 = [1,2,3,4,5,6]


jogarDado01 = lancar_dados(dado01)
jogarDado02 = lancar_dados(dado02)


print(f"o valor do 1º dado é: {jogarDado01}")
print(f"o valor do 2º dado é: {jogarDado02}")
print(f"a soma dos resultados dos dois dados é: {resultado(jogarDado01,jogarDado02)}")