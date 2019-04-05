__alunos__ = ['victor.bernardo@aluno.faculdadeimpacta.com.br',
              'roberto.filho@aluno.faculdadeimpacta.com.br'
              'bruno.avelino@aluno.faculdadeimpacta.com.br']

import math


class Ponto():
    '''
    Implementa a abstração de um ponto no plano Cartesiano 2D,
    que possui como atributos as coordenadas x e y
    '''

    def __init__(self, x: float, y: float) -> None:
        '''
        Construtor da classe
        '''
        self.x = x
        self.y = y

    def desloca(self, dx: float, dy: float) -> None:
        '''
        Desloca o ponto em dx no eixo x e dy no eixo y
        '''
        self.x += dx
        self.y += dy

    def distancia(self, ponto: 'Ponto') -> float:
        '''
        Calcula a distância euclidiana em relação a outro ponto
        passado como argumento
        '''
        d2 = (self.x - ponto.x) ** 2 + (self.y - ponto.y) ** 2
        return math.sqrt(d2)


class Reta():
    '''
    Cria a abstração de uma reta no plano cartesiano 2D e tem como atributos
    o coeficiente deincl
    '''
    def __init__(self, a: float, b: float):
        # y = a * x + b
        self.a = a
        self.b = b

    def pertence(self, ponto: Ponto) -> bool:
        '''
        Devolve 'True se o ponto pertence a reta e 'False' caso contrário
        '''
        # y = a x + b
        # y = 2x + 1
        return self.a * ponto.x + self.b == ponto.y

    def eh_paralela(self, reta: 'Reta') -> bool:
        '''
        Retorna true se a reta é paralela a esta reta e 'False' caso contrário
        '''
        # a = a
        return self.a == reta.a

    def interseccao(self, reta: 'Reta') -> Ponto:
        '''
        Retorna o ponto de intersecção com a reta passada como argumento
        caso não haja intersecção retorna 'None'
        '''
        # y = x + 1
        # y = 2x - 1
        # x = (self.a - reta.b) / (self.a - reta.b)
        # y = (self.a * x) + (self.b)
        # return Ponto(x, y)

    def perpendicular(self, ponto: Ponto) -> 'Reta':
        '''
        BÔNUS:
        Cria uma reta perpencidular à esta reta que passa por ponto
        '''
        pass


if __name__ == '__main__':
    r = Reta(2, 1)
    s = Reta(2, 2)
    print(r.eh_paralela(s))
    p = Ponto(1, 5)
    print(r.pertence(p))
    i = Reta(1, 0)
    d = Reta(-1, 0)
    print(i.interseccao(d))
