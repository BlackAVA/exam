import csv

with open('C:/Users/Kids01/Desktop/Вариант 18/languages.csv', encoding='utf8') as f:
    reader = list(csv.reader(f, delimiter=';'))[1::]
m = []
for i in range(len(reader)):
    R = int(reader[i][4]) / (2023 - int(reader[i][2]))
    m.append([reader[i][0], R])
print(m)