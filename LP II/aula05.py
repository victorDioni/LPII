'''
# criar um dicionario
dic = {}
dic2 = {'chave1': 'valor', 'chave': 'valor2'}

# acessar um item do dicionario
dic2['chave1']

# colocar um novo item em um dicionario
dic2['chave_nova'] = 'valor novo'

# modificar um item de um dicionario
dic2['chave_nova'] = 'novo_valor'

# remover um item de um dicionario
del(dic['chave1'])

# verificar se uma chave está no dicionario
'chave_teste' in dic2

# possibilidade de chaves e valores


# iterar sobre um dicionario

'''

import auxiliares as aux
biblia = {}

for linha in aux.le_biblia():
    for palavra in linha.split():
        if palavra not in biblia:
            biblia[palavra] = 1
        else:
            biblia[palavra] += 1
print(biblia)

maior = 0
freq = ''
for palavra in biblia:
    if biblia[palavra] > maior:
        maior = biblia[palavra]
        freq = palavra
print(freq, maior)
