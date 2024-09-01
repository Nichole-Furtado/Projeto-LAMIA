class Contador:
    contador = 0  # atributo de classe

    def inst(self):
        self.contador += 1 # mesma coisa q self.contador = self.contador + 1 que cria 1 atribudo no contador
        return 'Estou bem!'

    @classmethod
    def inc(cls):
        cls.contador += 1
        return cls.contador

    @classmethod
    def dec(cls):
        cls.contador -= 1
        return cls.contador
    
    @staticmethod
    def mais_um(cls,n):
        return n + 1

c1 = Contador()
# print(c1.inc_maluco()) 
# print(c1.inc_maluco())
# print(c1.inc_maluco())
# print(c1.inc_maluco())
 
# print (c1.inst())
# print(c1.inc())  # 1
# print(c1.inc())  # 2
# print(c1.inc())  # 3
# print(c1.dec())  # 2
# print(c1.dec())  # 1
# print(c1.dec())  # 0

# print(Contador.inc())  # 1
# print(Contador.inc())  # 2
# print(Contador.inc())  # 3
# print(Contador.dec())  # 2
# print(Contador.dec())  # 1
# print(Contador.dec())  # 0
# print(Contador.mais_um(99)) # 100