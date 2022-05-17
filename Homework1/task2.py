# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

list = []
number = int(input("Введите число N: "))
for n in range(2, number):
    if number % n == 0:
        list.append(n)

print(list)

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def factorization(n):
    i = 2
    primfac = []
    while i * i <= n:
        while n % i == 0:
            primfac.append(i)
            n = n / i
        i = i + 1
    if n > 1:
        primfac.append(n)
    return primfac


number = int(input('Inpunt number: '))
print(f'{factorization(number)}')
