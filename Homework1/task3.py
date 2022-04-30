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
