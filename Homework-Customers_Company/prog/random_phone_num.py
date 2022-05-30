import random


def generate_random_phone_number(length=8, minNumber=0, maxNumber=9):
    result = '+'
    for i in range(length):
        result += str(random.randint(minNumber, maxNumber))
    return result
