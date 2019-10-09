import json

data = []
data.append({
    'name': 'first',
    'color': 'red',
    'min_version': 1.1,
    'max_version': 1.3
})
data.append({
    'name': 'second',
    'color': 'blue',
    'min_version': 1.0,
    'max_version': 1.1
})
data.append({
    'name': 'third',
    'color': 'red',
    'min_version': 1.2,
    'max_version': 1.4
})
data.append({
    'name': 'fourth',
    'color': 'red',
    'min_version': 1.3,
    'max_version': 1.4
})
data.append({
    'name': 'fifth',
    'color': 'green',
    'min_version': 1.2,
    'max_version': 1.3
})
data.append({
    'name': 'sixth',
    'color': 'red',
    'min_version': 2.0,
    'max_version': 2.1
})
data.append({
    'name': 'seventh',
    'color': 'green',
    'min_version': 1.2,
    'max_version': 1.3
})

with open('mail_03Oct19\data.txt', 'w') as outfile:
    json.dump(data, outfile)