import json

def matchMachines(userFile='data.txt'):
    with open(userFile) as json_file:
        data = json.load(json_file)

    groups = []
    line = 0

    for machine in range(len(data)):
        add = True
        for j in groups:
            if data[machine]['name'] in j:
                add = False
                break
        if add:        
            color = data[machine]['color']
            minV = data[machine]['min_version']
            maxV = data[machine]['max_version']
            newGroup = data[machine]['name']
            for comparison in range(machine+1,len(data)):
                intersects = ((data[comparison]['min_version'] <= maxV and data[comparison]['min_version'] >= minV) or
                    (data[comparison]['max_version'] <= maxV and data[comparison]['max_version'] >= minV))
                if data[comparison]['color'] == color and intersects:
                    # If matches all conditions add 'name' to newGroup
                    newGroup += ' ' + data[comparison]['name']
            groups.append(newGroup)
    return groups

file = input('Insert file "path\\name.ext" (leave blank for default "data.txt"): ', )

if file:
    matches = matchMachines(file)
else:
    matches = matchMachines()
print('File path\\name: \\' + file)
for i in matches:
    print(i)