import random
class Sorteador:
    def __init__(self, nomes):
        self.nomes = nomes

    def sortear(self):
        return random.choice(self.nomes)
    
sorteador = Sorteador(["João", "Maria", "Pedro", "Ana"])
print (sorteador.sortear())
