class Carro:
    def __init__(self):
        self.__velocidade = 0 
    
    @property  
    def velocidade(self):
        return self.__velocidade
    
    @velocidade.setter
    def velocidade(self, valor):
        self.__velocidade = valor
    #método
    # vai acelerar de 5 em 5
    def acelerar(self):
        self.velocidade += 5
        return self.velocidade
    # frear de 5 em 5
    def frear(self):
        self.velocidade -= 5
        return self.velocidade
 
class Uno(Carro):
    pass

class Ferrari(Carro):
    def acelerar(self):
        # acelera duas vezes
        super().acelerar()
        super().acelerar()
        return self.velocidade 


c1 = Carro()
print(c1.acelerar())  # 5
print(c1.acelerar())  # 10
print(c1.acelerar())  # 15
print(c1.frear())     # 10
print(c1.frear())     # 5
