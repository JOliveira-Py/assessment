#!/usr/bin/env python3.6
""" Smallest Shared Range

Dadas várias listas ordenadas de inteiros positivos, determina o intervalo mais pequeno de
inteiros que é comum a todas as listas.
"""

# Check in which list (0, 1, ..., n) of 'lists[n]' the 'nr' is
def checkListIndex(nr, lists):
    for List in lists:
        if nr in List:
            return lists.index(List)

def sharedRange(lists):
    nrLists = len(lists)
    combinationList = []
    interval = []
    smallest = []
    rangeDiff = 0
    uniqueList = []
    [uniqueList.extend(content) for content in lists]
    uniqueList.sort()
    
    for nr in range(0, len(uniqueList)):
        interval.clear()
        combinationList.clear()
        jump = False
        # Check if 'nr' in analisys is within the same list as nexts 'nr'(s), if so no need to check
        # an interval with it
        for i in range(1,nrLists):
            try:
                if checkListIndex(uniqueList[nr],lists) == checkListIndex(uniqueList[nr+i],lists):
                    jump = True
                    break
            except:
                break
        if jump:
            continue
        
        interval.append(uniqueList[nr])
        combinationList.append(checkListIndex(uniqueList[nr],lists))
        # Search/Build the 'smallest' interval common to all 'lists[n]'
        for nr2 in range(nr+1, len(uniqueList)):
            if checkListIndex(uniqueList[nr2], lists) not in combinationList:
                interval.append(uniqueList[nr2])
                combinationList.append(checkListIndex(uniqueList[nr2],lists))
                if len(combinationList) == nrLists:
                    interval.sort()
                    if not rangeDiff:
                        rangeDiff = interval[-1] - interval[0]
                        smallest = [interval[0], interval[-1]]
                    elif interval[-1]-interval[0] < rangeDiff:
                        rangeDiff = interval[-1] - interval[0]
                        smallest = [interval[0], interval[-1]]
                    break
    return smallest


defaultVar = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
print(sharedRange(defaultVar))