import csv

with open('students.csv', encoding='utf8') as f:
    reader = list(csv.DictReader(f, delimiter=',', quotechar='"'))
    for i in range(len(reader)):
        j = i - 1
        key = reader[i]
        while float(reader[j]['score'] if reader[j]['score'] != 'None' else 0) < float(key['score'] if key['score'] != 'None' else 0) and j >= 0:
            reader[j+1] = reader[j]
            j -= 1
        reader[j+1] = key
print('10 класс')
c = 1
for i in reader:
    if '10' in i['class']:
        surname, name, patronumic = i["Name"].split()
        print(f"{c} место: {name[0]}. {surname}")
        c += 1
    if c == 4:
        break