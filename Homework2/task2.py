# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота "интеллектом"

from random import randint, random


candies = 2021
while (candies > 0):

    print('Первый игрок берет конфеты, но не более 28 шт.!')
    user_1 = int(randint(1, 28))
    print(user_1)
    print()
    print('Второй игрок берет конфеты, но не более 28 шт.!')
    user_2 = int(randint(1, 28))
    print(user_2)
    print()
    candies -= user_1 + user_2
    print()
    if candies < 0 or user_1 > candies or user_2 > candies:

        break

print('Игра окончена! Осталось ', candies, ' конфет')
