class Animal:
    def __init__(self,nome):
      self.nome= nome
    def falar(self):
       return "animais fazem som"

class Cachorro(Animal):
   def falar(self):
      return ("Au,Au")
   
class Gato(Animal):
   def falar(self):
      return ("meau,meau")
rex = Cachorro("rex")
chanim = Gato("chanim")
   
print(f"o cachorro {rex.nome} faz {rex.falar()}")
print(f"o gato {chanim.nome} faz {chanim.falar()}")