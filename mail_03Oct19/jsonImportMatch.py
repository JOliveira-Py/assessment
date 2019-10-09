import json

with open('data.txt') as json_file:
    data = json.load(json_file)
    groups = []
    for machine in range(0, len(data['machines'])):
        print(groups)
        if not groups:
            groups.append([machine])
            groups[machine] = ['krist0']
            #groups.append(machine+1)
            #groups[machine+1] = ['krist0las']
            print('1º'+str(groups[0]))

        for i in groups:
            print("blabla" + str(groups))
            print('2º'+str(i))
            if data['machines'][machine]['name'] not in i:
                color = data['machines'][machine]['color']
                minV = data['machines'][machine]['min_version']
                maxV = data['machines'][machine]['max_version']
                groups.append([machine])
                print('machine =' + str(machine))
                groups[machine] = [data['machines'][machine]['name']]
                print("check" + str(groups[machine]))
                for compare in range(machine+1, len(data['machines'])):
                    for key, value in data['machines'][compare].items():
                        if key == 'color' and value == color and data['machines'][compare]['name'] not in groups:
                            groups[machine].append(data['machines'][compare]['name'])
                    if compare == len(data['machines'])-1:
                        print(str(machine) + '-' + str(compare))
                        print(groups[machine])
            else:
                print('duh')