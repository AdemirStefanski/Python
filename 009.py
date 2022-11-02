def escrever_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo , 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo , 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo , 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    aluno_nota = aluno_nota.split('\n')
    #print(aluno_nota)
    lista_media = []

    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        #print(aluno)
        #print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas])/4
        #print('Aluno {} teve as notas: {} e média: {}\n' .format(aluno, lista_notas, media(lista_notas)))
        lista_media.append({aluno: media(lista_notas)})
    return lista_media

if __name__ == '__main__':
    lista_media = media_notas('notas.txt')
    print(lista_media)
    #escrever_arquivo('Primeira linha.\n')
    #aluno = 'Keito 10,8,10,10\n'
    #atualizar_arquivo('notas.txt' , aluno)
    #ler_arquivo('texto.txt')

