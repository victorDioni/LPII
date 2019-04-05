# Correção do calendario professor que fez
class Data():
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.meses = {1: 31, 2: 28, 3: 31, 4: 30,
                      5: 31, 6: 30, 7: 31, 8: 31,
                      9: 30, 10: 31, 11: 30, 12: 31}

    def imprimi_data(self):
        print("{:02d}/{:02d}/{:04d}".format(self.dia, self.mes, self.ano))

    def proximo_ano(self):
        self.ano += 1      

    def amanha(self):
        if self.dia < self.meses[self.mes]:
            self.dia += 1
        else:
            self.dia = 1
            if self.mes == 12:
                self.mes = 1
                self.ano += 1 
            else:
                self.mes += 1

    def proxima_semana(self):
        self.amanha()
        self.amanha()
        self.amanha()
        self.amanha()
        self.amanha()
        self.amanha()
        self.amanha()

if __name__ == '__main__':

    data = Data(31, 12, 2019)

    data.imprimi_data()
    
    data.imprimi_data()
    data.amanha()
    data.imprimi_data()
