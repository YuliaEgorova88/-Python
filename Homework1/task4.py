# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 1 до 100, можно создать свой генератор случайных чисел или использовать готовый) многочлена и записать в файл многочлен степени k.

# Пример:

# k=2 => 2*x² + 4*x + 5 = 0

from random import randint, random
from readline import write_history_file


step = int(input("Введите степень числа: "))
coeff = randint(1, 100)


def stepen(step):
    while step >= 3:
        step -= 1
    return step


print('K = ', step, '=> ', coeff, '* x ^',
      stepen(step), '+ ', coeff, '* x ^', stepen(step))
