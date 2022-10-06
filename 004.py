num1 = int(input('Entre com a quantidade de números primos que deseja: '))
num2 = int(input('Entre com o valor inicial:'))
num3 = int(input('Entre com o valor final:'))
while num3 <= num2:
    num3 = int(input('O valor final deve ser maior que o valor inicial Digite novamente: '))
x=1
a =1
for x in range(num2, num3+1):
    div = 0
    for y in range (1,x+1):
        resto = x % y
        if resto == 0:
            div +=1
    if div == 2 and a <= num1:
        print(y)
        a +=1