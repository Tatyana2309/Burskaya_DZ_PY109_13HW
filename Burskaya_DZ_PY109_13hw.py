# task 1

with open('example.txt') as f: # открываем файл
    file_1 = f.read().split(' ') # читаем файл
sum_new = 0
for i in file_1: # разбиваем файлы
    if i.isdigit(): # если индекс в файле число
        sum_new += int(i) # находим сумму
print(f'Сумма чисел равна: {sum_new}')

# task 2
f = open('example1.txt') # открываем файл
list_2 = [] # создаем пустые списки
list_3 = []
list_1 = f.readlines() # читаем все строки файла
print(list_1)
for i in list_1: # создаем новые списаки со словами и числами
    i = i[:-1]
    if i.isdigit():
        list_2.append(int(i))
    elif i.isalpha():
        list_3.append(str(i))
print(list_2)
print(list_3)
list_2.sort() # сортируем числа по возрастанию
list_3.sort(key=len) # сортируем слова по длине символов
sum_1 = list_2 + list_3
print(sum_1)


# task 3
f = open('example2.txt', 'w') # открываем файл
while True:
    user_text = input("Введите строку: ")
    if user_text == "":
        break
    f.write(user_text + '\n') # записываем в файл строки пока пользователь не введет пустую строку
f.close()
#
# # task 4
f = open('example1.txt')
lines_1 = f.readlines() # читаем все строки файла
print(f'Количество строк равно: {len(lines_1)}') # находим кол-во строк в файле
for i in lines_1:
    print(f'Количество символов в строке равно: {len(i)}') # находим кол-во символов в строке
f.close()

# homework
f = open('homework_13.txt', 'w') # открываем файл для записи
list_hw = ['33', 'weather', '66', 'cold', 'you', '10', 'want', '45', 'spring']
list_2 = [] # создаем массив заполненный и 2 пустых листа для чисел и слов
list_3 = []
for i in list_hw: # добавляем в отдельные списпи слова и числа
    if i.isdigit():
        list_2.append(i)
    elif i.isalpha():
        list_3.append(i)
print(list_2)
print(list_3)
list_2.sort()  # сортируем числа по возрастанию
list_3.sort(key=len)  # сортируем слова по длине
sum_1 = list_3 + list_2  # складываем два списка
delimiter = '\n' # добавляем разделитель
delimiter_sum = delimiter.join(sum_1)  # выводим из списка строки
print(delimiter_sum)
f.write(delimiter_sum)  # записываем в файл данные
f.close() #  закрываем файл
