#!/usr/bin/python3.6

import json
from pathlib import Path

def intersects(a,b,c,d):
    return ((a <= c <= b)
            or (a <= d <= b)
            or (c <= a <= d)
            or (c <= b <= d))

def matchMachines(data):
    groups = []
    
    for machine in range(len(data)):
        add = True
        # Check if 'machine' was already matched
        for j in groups:
            if data[machine]['name'] in j:
                add = False
                break
        if add:        
            # Store info about original 'machine'
            color = data[machine]['color']
            minV = data[machine]['min_version']
            maxV = data[machine]['max_version']
            # Matching machines will be stored here
            newGroup = data[machine]['name']
            for comparison in range(machine+1,len(data)):
                added = False
                for k in groups:
                    if data[comparison]['name'] in k:
                        added = True
                        break
                if not added:
                    # Store info about 'comparison' machine
                    minV2 = data[comparison]['min_version']
                    maxV2 = data[comparison]['max_version']
                    if data[comparison]['color'] == color and intersects(minV,maxV,minV2,maxV2):
                        checkAllGroup = True
                        # Check if 'comparison' machine is version compatible with all
                        # machines previously added to current 'newGroup'
                        for m in data:
                            if m['name'] in newGroup:
                                minV3 = m['min_version']
                                maxV3 = m['max_version']
                                if not intersects(minV2,maxV2,minV3,maxV3):
                                    checkAllGroup = False
                                    break
                        # Add 'comparison' machine to matching machines 'newGroup'
                        if checkAllGroup:
                            newGroup += ' ' + data[comparison]['name']
            # Store 'newGroup' of matching machines
            groups.append(newGroup)
    return groups

file = input('Insert file "folder/file.ext" (leave blank for default "last_test.json"): ')

if not file:
    file = Path('data.txt')
with open(file) as json_file:
        fileData = json.load(json_file)
matches = matchMachines(fileData)
for i in matches:
    print(i)