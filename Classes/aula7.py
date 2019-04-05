# Como definir uma nova classe
class ClasseTeste():
    def __init__(self, valor1, valor2, valor3):
        self.atr = valor2, valor3, valor1
                
# definindo construtor __init__():
# pass é uma palavra que informa que não tem nada ou sej, passa reto não tem
# nada aqui

# Instanciando um obejto da classe definida


obj1 = ClasseTeste(13, 12, 11)
obj2 = ClasseTeste(11, 12, 13)
obj1.atr = 10
print(obj1.atr)
print(obj2.atr)
print(type(obj1) == type(obj2))


# objetos são instancias unicas, não são iguais


print(type(obj1))

lista = list()

print(type(lista))
