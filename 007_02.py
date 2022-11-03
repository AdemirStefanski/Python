num1 = int(input('Entre com o valor A: '))
num2 = int(input('Entre com o valor B: '))

class Calculadora:
    def __init__(self):
        pass

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

calculadora = Calculadora()

lista = [1, 2, 3, 4]
operacao = ''
#operacao = input('\nQual operação deseja realizar?\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n\nOperação: ')

while operacao not in lista:
    operacao = int(input('\nQual operação deseja realizar?\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n\nOperação: '))

operacao = str(operacao)

match operacao:
    case '1':
        print('\nSoma: {}' .format(calculadora.soma(num1, num2)))
    case '2':
        print('\nSubtração: {}' .format(calculadora.subtracao(num1,num2)))
    case '3':
        print('\nMultiplicação: {}' .format(calculadora.multiplicacao(num1,num2)))
    case '4':
        print('\n Divisão: {}' .format(calculadora.divisao(num1,num2)))

