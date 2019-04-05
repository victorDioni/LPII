def eh_primo(n):
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True


def lista_primos(n):
    lista = []
    for i in range(2, n):
        if eh_primo(i):
            lista.append(i)
    return lista


def fatora_primos(n):
    if eh_primo(n):
        # return [n]
        return [[n, 1]]
    lista = []
    for i in lista_primos(n//2+1):
        pot = 0
        while n % i == 0:
            pot += 1
            # lista.append(i)
            n = n // i
        if pot > 0:
            lista.append([i, pot])
    return lista


def main():
    print(__name__)
    print(fatora_primos(1024))


if __name__ == "__main__":
    main()
