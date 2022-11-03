from datetime import date, time, datetime, timedelta

def trabalhando_datetime():
    data_atual = datetime.now()
    print(data_atual)
    tupla = ('Segunda' , 'Terça' , 'Quarta' , 'Quinta' , 'Sexta' , 'Sábado' , 'Domingo')
    print(tupla[data_atual.weekday()])
    #usamos a tupla para converter o dia da semana em português. Podemos usar esse sistema com o mês.
    data_string = '18/04/1985 13:15:45'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    #utilizamos esse processo para converter uma data passada em str para uma data em int.
    print('\nData convertida: {}' .format(data_convertida))
    print('\nTipo de variável: {}'. format(type(data_convertida)))
    nova_data = data_convertida - timedelta(days=365, hours=3, minutes=2, seconds=10)
    #timedelta serve para fazer operações com o datas (-)subtração e (+)adição
    # Para cálculos com dias, mês e anos temos que converter em dias(não trabalha com mês e anos).
    #timedelta podemos também trabalhar com subtração de horas, minutos e segundos.

    print('\nData com as operações matemáticas aplicadas: {} ' .format(nova_data))

def trabalhando_time():
    horario = time(hour=14, minute=25, second=45)
    print(horario)

def trabalhando_date():
    data_atual = date.today()
    print(data_atual)
    data_atual_custom = data_atual.strftime('%A, %B, %Y')
    # a partir do momento que usar o strftime os dados passam a ser str e não int.
    print(data_atual_custom)

if __name__ == '__main__':
    trabalhando_datetime()
    #trabalhando_time()
    #trabalhando_date()
