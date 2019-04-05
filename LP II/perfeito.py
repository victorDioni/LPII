def lista_divisores(n):
    lista = []
    for i in range(1, n//2+1):
        if n % i == 0:
            lista.append(i)
    return lista


def eh_perfeito(n):
    lista = lista_divisores(n)
    soma = sum(lista)
    if soma == n:
        return True
    else:
        return False


def lista_perfeitos(n):
    lista = []
    for i in range(2, n + 1):
        if eh_perfeito(i):
            lista.append(i)
    return lista


def lista_n_perfeitos(n):
    lista = []
    i = 2
    while len(lista) < n:
        if eh_perfeito(i):
            lista.append(i)
        i += 1
    return lista


def lista_perfeitos_e_divisores(n):
    lista = []
    for i in range(2, n + 1):
        if eh_perfeito(i):
            lista.append([i, lista_divisores(i)])
    return lista


# print(lista_n_perfeitos(3))
