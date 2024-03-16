import csv

with open('C:/Users/Kids01/Desktop/Вариант 18/languages.csv', encoding='utf8') as f:
    reader = list(csv.reader(f, delimiter=';'))[1::]
m = {}
for i in reader:
    m[i[0]] = [i[3], i[2]]
a = input()
while a != '0':
    if a in m:
        print(a, 'был создан', m[a][0], 'в', m[a][1])
    else:
        print('Хм.. Вы уверены, что слышали об этом ЯП?')
    a = input()