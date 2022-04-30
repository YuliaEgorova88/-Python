# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

list = []
number = int(input("Введите число N: "))
for n in range(2, number):
    if number % n == 0:
        list.append(n)

print(list)
