import csv


with open('C:/Users/Kids01/Desktop/Вариант 18/languages.csv', encoding='utf8') as f:
    reader = list(csv.reader(f, delimiter=';'))[1::]
t = 0
for i in range(len(reader)):
    print('Книг для изучения', reader[i][0], 'в библиотеке нашлось:', reader[i][4])
    if reader[i][1] == 'язык запросов':
       t += int(reader[i][4])
print('Для изучения этой темы можно воспользоваться', t, 'книгами')\


