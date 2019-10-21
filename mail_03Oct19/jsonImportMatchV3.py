#!/usr/bin/python3.6

import json

def matchMachines(userFile='data.txt'):
    with open(userFile) as json_file:
        data = json.load(json_file)

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
                    intersects = (
                        (minV <= data[comparison]['min_version'] <= maxV)
                        or (minV <= data[comparison]['max_version'] <= maxV)
                        or (data[comparison]['min_version'] <= minV <= data[comparison]['max_version'])
                        or (data[comparison]['min_version'] <= maxV <= data[comparison]['max_version']))
                    if data[comparison]['color'] == color and intersects:
                        checkAllGroup = True
                        # Store info about 'comparison' machine
                        minV2 = data[comparison]['min_version']
                        maxV2 = data[comparison]['max_version']
                        # Check if 'comparison' machine is version compatible with all
                        # machines previously added to current 'newGroup'
                        for m in data:
                            if m['name'] in newGroup:
                                intersectsAlso = (
                                    (minV2 <= m['min_version'] <= maxV2)
                                    or (minV2 <= m['max_version'] <= maxV2)
                                    or (m['min_version'] <= minV2 <= m['max_version'])
                                    or (m['min_version'] <= maxV2 <= m['max_version']))
                                if not intersectsAlso:
                                    checkAllGroup = False
                                    break
                        # Add 'comparison' machine to matching machines 'newGroup'
                        if checkAllGroup:
                            newGroup += ' ' + data[comparison]['name']
            # Store 'newGroup' of matching machines
            groups.append(newGroup)
    return groups

file = input('Insert file "path\\name.ext" (leave blank for default "data.txt"): ')

if file:
    matches = matchMachines(file)
else:
    matches = matchMachines()
for i in matches:
    print(i)
