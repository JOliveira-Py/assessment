#!/usr/bin/env python3

def checkListNr(nr, lists):
    for listNr in range(0, len(lists)):
        if nr in lists[listNr]:
            return listNr

def sharedRange(lists):
    nrLists = len(lists)
    combination = []
    interval = []
    smallest = []
    rangeDiff = 0
    uniqueList = []
    [uniqueList.extend(content) for content in lists]
    uniqueList.sort()
    for nr in range(0, len(uniqueList)):
        interval.clear()
        combination.clear()
        interval.append(uniqueList[nr])
        combination.append(checkListNr(uniqueList[nr],lists))
        for nr2 in range(nr+1, len(uniqueList)):
            if checkListNr(uniqueList[nr2], lists) not in combination:
                interval.append(uniqueList[nr2])
                combination.append(checkListNr(uniqueList[nr2],lists))
                if len(combination) == nrLists:
                    interval.sort()
                    if not nr:
                        rangeDiff = interval[-1] - interval[0]
                        smallest = [interval[0], interval[-1]]
                    elif interval[-1]-interval[0] < rangeDiff:
                        rangeDiff = interval[-1] - interval[0]
                        smallest = [interval[0], interval[-1]]
                    break
    return smallest


defaultVar = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
print(sharedRange(defaultVar))