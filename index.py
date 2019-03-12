import json
with open('table.json') as jsonTable:
    t = json.load(jsonTable)
    jsonTable.close()
strings = list(dict.keys(t));
a = [1,2,3,4]
for i in a:
    print(i)
