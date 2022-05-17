# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from array import array
from posixpath import split


myList = []


list = input("Введите числа: ").split()

for i in range(len(list)):
    old = list[i]
    new = int(old)
    list[i] = new
    myList.append(list[i])
print(myList)


def uniqueNumbers(myList):
    myNewList = []
    for sym in myList:
        if sym in myNewList:
            continue
        else:
            myNewList.append(sym)
    return myNewList


print(uniqueNumbers(myList))


# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.


# Запрашиваем строку с числами
string = input('Input array [example: 1 2 4 2 5 6]: ')

# Преобразование строки в список чисел
array = string.split(' ')

# Словарь, в котором будем хранить все
# включения чисел в строке вида {   1 : 2,
#                                   4 : 6
#                               }
# где key - это числа, а value - количество повторений в списке
dictionary = {}

# переменная нужна для регистрации, есть ли данное число в словаре
flag = True

# Циклом проходим по списку с числами
for i in range(0, len(array)):
    flag = True  # Обнуление переменной
    for j in dictionary.keys():  # Цикл проходит по ключам словаря
        if(j == array[i]):  # Если значение ключа в словаре соответствует значению в списке (числу)
            dictionary[j] += 1  # Увеличиваем
            flag = False  # Если в словаре нашёлся необходимый ключ, переменная меняет значение
            continue
    if flag:  # Если в словаре не нашлось ключа-числа, добавляем это число в словарь
        dictionary[array[i]] = 1

# Вывод всех ключей словаря, значения которых равны единице
for i in dictionary:
    if (dictionary[i] == 1):
        print(f'{i}', end=' ')
