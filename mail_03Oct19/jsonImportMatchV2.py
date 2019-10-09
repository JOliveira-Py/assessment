import json

with open('data2.txt') as json_file:
    data = json.load(json_file)

groups = ['']
line = 0

for machine in range(len(data)):
    for j in groups:
        print('JOTA IN GROUPS = ' + str(j))
        if data[machine]['name'] in j:
            print(data[machine]['name'] + ' IS in groups')
            add = False
            break
        else:
            print(data[machine]['name'] + ' NOT in groups')
            add = True
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
                print(newGroup)
        groups.append(newGroup)
for i in groups:
    print('groups ' + str(i))

   
   