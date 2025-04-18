class veiculo:
    def __init__(self,nome):
       self.nome = nome
    def movimentar(self):
        return "veiculo em movimento"
    
class carro(veiculo):
    def movimentar(self):
        return " está dirigindo"
    
class moto(veiculo):
    def movimentar(self):
        return "está acelerando"
    
gol = carro("gol")
cb300 = moto("Cb 300")
    
print(f"{gol.nome} {gol.movimentar()}")
print(f"{cb300.nome} {cb300.movimentar()}")

    