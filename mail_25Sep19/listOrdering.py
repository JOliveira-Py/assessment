def top3(list):
    intList = [int(i) for i in list]
    intList.sort(reverse=True)
    return intList[0:3]

 
scoresList = []

while True:
    print('Insert score nr ' + str(len(scoresList)+1) + ': (or leave it blank to finish)')
    score = input()
    if score == '':
        break
    else:
        scoresList = scoresList + [score]
    
print("Top Score:\n" + str(top3(scoresList)[0]) + "\n")
print("Top3:\n" + str(top3(scoresList)) + "\n")
print("Last score inserted:\n" + scoresList[-1])