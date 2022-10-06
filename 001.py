print('\nCalculadora de DOIS números. Soma, Subtração, Multiplicação, Divisão e Resto')

a = int(input('\nEntre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
# a = 10 começei com variáveis fixas e mudei para o usuário inseri-la.
# b = 5  começei com variáveis fixas e mudei para o usuário inseri-la.
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

# print('soma: ' + soma) não tem como imprimir pois 'soma' é uma string e a variável soma é uma variável numérica, no caso INT.
# print(soma)  mudei o jeito de saída para usar o format e com isso ficar mais elegante.
# print(subtracao)
# print(multiplicacao)
# print(divisao)
# print(resto)

print('\nSoma: {sum} \nSubtração {sub} \nMultiplicação {mult}'
      '\nDivisão: {div} \nResto: {rem}  ' .format(sum=soma, sub=subtracao,
                                                rem = resto, div = divisao,
                                                mult = multiplicacao))