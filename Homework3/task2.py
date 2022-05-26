# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Задайте натуральное число N: '))
n1 = n
res = []
# numbers = []
# for i Input_data range (2, int(math.sqrt(n))+1):
#     while (n1 % i == 0):
#         numbers.append(i)
#         n1 //= i
# if (n1 != 1):
#     numbers.append(n1)
# print(f'Простые множители числа {n}: ', numbers)


def func(i):
    global n1
    global res
    a = []
    while (n1 % i == 0):
        n1 //= i
        res.append(i)


list(map(func, [i for i in range(2, int(n**0.5)+1)]))
if (n1 != 1):
    res.append(n1)

print(res)
