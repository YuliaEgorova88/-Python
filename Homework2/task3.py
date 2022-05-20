# 3. Создайте программу для игры в "Крестики-нолики".


# Инициализация карты
maps = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]


# Инициализация победных линий
victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]


# Вывод карты на экран
def print_maps():
    print(maps[0], end=" ")
    print(maps[1], end=" ")
    print(maps[2])

    print(maps[3], end=" ")
    print(maps[4], end=" ")
    print(maps[5])

    print(maps[6], end=" ")
    print(maps[7], end=" ")
    print(maps[8])


# Сделать ход в ячейку
def step_maps(step, symbol):
    ind = maps.index(step)
    maps[ind] = symbol


# Получить текущий результат игры
def get_result():
    win = ""

    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "Игрок 1"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "Игрок 2"

    return win


# Основная программа
game_over = False
player1 = True

while game_over == False:

    # 1. Показываем карту
    print_maps()

    # 2. Спросим у играющего куда делать ход
    if player1 == True:
        symbol = "X"
        step = int(input("Игрок 1, ваш ход: "))
        print()
    else:
        symbol = "O"
        step = int(input("Игрок 2, ваш ход: "))
        print()

    step_maps(step, symbol)  # делаем ход в указанную ячейку
    win = get_result()  # определим победителя
    if win != "":
        game_over = True
    else:
        game_over = False

    player1 = not(player1)

# Игра окончена. Покажем карту. Объявим победителя.
print_maps()
print()
print("Победил", win)
print()
######################

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def game(mass): return print(' | ', mass[0], ' | ', mass[1], ' | ', mass[2], ' | \n | ', mass[3],
                             ' | ', mass[4], ' | ', mass[5], ' | \n | ', mass[6], ' | ', mass[7], ' | ', mass[8], ' | ')


k = 0


def win(mass):
    if (mass[0] == mass[1] == mass[2] == 'X') or (mass[3] == mass[4] == mass[5] == 'X') or (mass[6] == mass[7] == mass[8] == 'X') or (mass[0] == mass[3] == mass[6] == 'X') or (mass[1] == mass[4] == mass[7] == 'X') or (mass[2] == mass[5] == mass[8] == 'X') or (mass[0] == mass[4] == mass[8] == 'X') or (mass[2] == mass[4] == mass[6] == 'X'):
        return 1
    elif (mass[0] == mass[1] == mass[2] == 'O') or (mass[3] == mass[4] == mass[5] == 'O') or (mass[6] == mass[7] == mass[8] == 'O') or (mass[0] == mass[3] == mass[6] == 'O') or (mass[1] == mass[4] == mass[7] == 'O') or (mass[2] == mass[5] == mass[8] == 'O') or (mass[0] == mass[4] == mass[8] == 'O') or (mass[2] == mass[4] == mass[6] == 'O'):
        return 1
    else:
        return 0


print("Игра крестики - нолики")
game(list)
while k <= 9:
    k += 1
    x1 = int(input("Ход игрока №1. В какое поле ставим X: "))
    if list[x1-1] == 'X' or list[x1-1] == 'O':
        x1 = int(input("Поле занято. Введите номер свободного поля: "))
        list[x1-1] = 'X'
    else:
        list[x1-1] = 'X'
    game(list)
    if win(list):
        print('Игрок №1 победил!')
        break
    if k == 9:
        break
    k += 1
    x1 = int(input("Ход игрока №2. В какое поле ставим O: "))
    if list[x1-1] == 'X' or list[x1-1] == 'O':
        x1 = int(input("Поле занято. Введите номер свободного поля: "))
        list[x1-1] = 'O'
    else:
        list[x1-1] = 'O'
    game(list)
    if win(list):
        print('Игрок №2 победил!')
        break
if win(list):
    print("Спасибо за игру!")
else:
    print("Ничья! Спасибо за игру!")

###################
