import csv

with open('students.csv', encoding='utf8') as f:
    reader = list(csv.DictReader(f, delimiter=',', quotechar='"'))
    data = sorted(reader, key=lambda  x: x['titleProject_id'])

id_project = input()
while id_project != 'СТОП':
    id_project = int(id_project)
    for i in data:
        if int(i['titleProject_id']) == id_project:
            surname, name, patronumic = i["Name"].split()
            print(f'Проект № {id_project} делал: {name[0]}. {surname} он(а) получил(а) оценку - {i["score"]}.')
            break
    else:
        print('Ничего не найдено')
    id_project = input()