def top3(list):
    intList = [int(i) for i in list]
    intList.sort(reverse=True)
    return str(intList[0:3])

#without using 'list.sort' method
def top1(list):
    aux = int(list[0])
    for i in list:
        if int(i) > int(aux):
            aux = i
    return aux
    

scoresList = []

while True:
    print('Insert score nr ' + str(len(scoresList)+1) + ': (or leave it blank to finish)')
    score = input()
    if score == '':
        break
    else:
        scoresList = scoresList + [score]
    
print("Top Score:\n" + str(top1(scoresList)) + "\n")
print("Top3:\n" + top3(scoresList) + "\n")
print("Last score inserted:\n" + scoresList[-1])

