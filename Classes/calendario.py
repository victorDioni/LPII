class Data:
    dia = None
    mes = None
    ano = None

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def imprimi_data(self):
        print(self.dia)
        print(self.mes)
        print(self.ano)


hoje = Data(29, 3, 2019)

print(hoje.imprimi_data())
