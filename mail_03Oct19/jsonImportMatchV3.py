import json

def matchMachines(userFile='data.txt'):
    with open(userFile) as json_file:
        data = json.load(json_file)

    groups = []

    for machine in range(len(data)):
        add = True
        # Check if machine was already matched
        for j in groups:
            if data[machine]['name'] in j:
                add = False
                break
        if add:        
            # Store info about 'original' machine
            color = data[machine]['color']
            minV = data[machine]['min_version']
            maxV = data[machine]['max_version']
            # Matching machines will be stored here
            newGroup = data[machine]['name']
            for comparison in range(machine+1,len(data)):
                intersects = (
                    (minV <= data[comparison]['min_version'] <= maxV)
                    or (minV <= data[comparison]['max_version'] <= maxV))
                if data[comparison]['color'] == color and intersects:
                    # Add new machine to matching machines
                    newGroup += ' ' + data[comparison]['name']
            # Store new group of matching machines
            groups.append(newGroup)
    return groups

file = input('Insert file "path\\name.ext" (leave blank for default "data.txt"): ')

if file:
    matches = matchMachines(file)
else:
    matches = matchMachines()
for i in matches:
    print(i)