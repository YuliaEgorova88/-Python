# Вычислить число Пи c заданной точностью d
# Пример:
#
# при $d = 0.001, π = 3.141.$ $10^{-1} ≤ d ≤10^{-10}$


# Импорт библиотеки math
import math

# Функция для преобразования точности вида 0.001 => 3


def accuracy(data):
    i = 0
    while 1 > data:
        i += 1
        data = data * 10
    return i


def accuracyPI(precision):
    return round(math.pi, precision)


precision = float(input('Input precision (example: 0.001): '))
print(f'{AccuracyPI(Accuracy(precision))}')
