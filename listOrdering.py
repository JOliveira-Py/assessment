def top3(lista):
    listaInt = [int(i) for i in lista]
    listaInt.sort(reverse=True)
    return str(listaInt[0:3])

#sem utilizar a função 'sort'
def top1(lista):
    aux = int(lista[0])
    for i in lista:
        if int(i) > int(aux):
            aux = i
    return aux
    

listaPontuacoes = []

while True:
    print('Introduza a ' + str(len(listaPontuacoes)+1) + 'ª pontuação (ou deixe em branco para terminar)')
    pontuacao = input()
    if pontuacao == '':
        break
    else:
        listaPontuacoes = listaPontuacoes + [pontuacao]
    
print("Pontuação mais alta:\n" + str(top1(listaPontuacoes)) + "\n")
print("Top3:\n" + top3(listaPontuacoes) + "\n")
print("Última pontuação inserida:\n" + listaPontuacoes[-1])

