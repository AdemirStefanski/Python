n1 = int(input('Entre com o valor a ser adicionado no conjunto 1 ou 00 para sair: '))
conjunto1 = set()
conjunto1.add(n1)
while n1 != 00:
    n1 = int(input('Entre com o valor a ser adicionado no conjunto 1 ou 00 para sair: '))
    conjunto1.add(n1)

n2 = int(input('Entre com o valor a ser adicionado no conjunto 2 ou 00 para sair: '))
conjunto2 = set()
conjunto2.add(n2)
while n2 != 00:
    n2 = int(input('entre com o valor a ser adicionado no conjunto 2 ou 00 para sair: '))
    conjunto2.add(n2)

conjunto2.remove(0)
conjunto1.remove(0)
print('\nConjunto 1 {}' .format(conjunto1))
print('Conjunto 2 {}' .format(conjunto2))

op = int(input('\nQual operação você quer fazer com os conjuntos?\n1 - União. \n2 - Intersecção. \n3 - Diferença. \n4 - Diferença Simétrica. \n0 - Sair. \nEntre com a opção(1-4):'))
while op != 0:
    match op:
        case 0:
            quit()
        case 1:
            conjunto3 = conjunto1.union(conjunto2)
            print('\nUnião entre os dois conjuntos: {}' .format(conjunto3))
        case 2:
            conjunto4 = conjunto1.intersection(conjunto2)
            print('\nIntersecção entre os dois conjuntos: {}' .format(conjunto4))
        case 3:
            conjunto5 = conjunto1.difference(conjunto2)
            print('\nDiferença do conjunto 1 para com o conjunto 2: {}' .format(conjunto5))
        case 4:
            conjunto6 = conjunto1.symmetric_difference(conjunto2)
            print('\nDiferença simétrica entre os dois conjuntos: {}' .format(conjunto6))
    op = int(input('\nQual operação você quer fazer com os conjuntos?\n1 - União. \n2 - Intersecção. \n3 - Diferença. \n4 - Diferença Simétrica. \n0 - Sair. \nEntre com a opção(1-4):'))

