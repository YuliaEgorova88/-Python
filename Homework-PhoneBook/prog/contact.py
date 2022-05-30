import pickle
import random
import string

from Homework5.input.user_answer import get_user_name, get_phone_number, read_user_answer

contact_list = []


def save_contact():
    global contact_list
    path = 'contacts'
    try:
        with open(path, 'wb') as data:
            pickle.dump(contact_list, data)
    except:
        print('Ошибка при записи контакта в файл')


def add_contact():
    global contact_list
    NumberText = '\n1 - Добавить еще контакт \n0 - Выйти в главное меню \nВыберите операцию: '
    f = True
    while f:
        print('\nДобавить контакт')
        contact_list.append({'Name': get_user_name(), 'Phone Number': get_phone_number()})
        f = end_program(NumberText)
    save_contact()


def show_contacts(is_end_prog=False):
    global contact_list
    NumberText = '\n1 - Обновить список контактов \n0 - Выйти в главное меню \nВыберите операцию: '
    f = True

    if is_end_prog:
        print('\nСписок контактов ')
        read_data()
    else:
        while f:
            print('\nСписок контактов ')
            read_data()
            f = end_program(NumberText)


def load_contacts(f=True):
    global contact_list
    path = 'contacts'
    try:
        with open(path, 'rb') as data:
            contact_list = pickle.load(data)
    except:
        if not f:
            print()
        else:
            print('Нету сотрудников!')
            return False
    return True


def read_data():
    global contact_list
    counter = 1
    print()
    for i in contact_list:
        print(f'{counter} - ', end='')
        for key, value in i.items():
            print(f'{key}: {value}', end=', ')
        print()
        counter += 1
    print(f'Обшее количество контактов {len(contact_list)}')


def del_contact():
    global contact_list
    NumberText = '\n1 - Удалить еще контакт \n0 - Выйти в главное меню \nВыберите операцию: '
    f = True
    while f:
        print('\nУдалить контакт ')
        show_contacts(True)
        read_user_answer_text = 'Выберите цифру контакта: '
        user_answer = read_user_answer(read_user_answer_text, minNumber=1, maxNumber=len(contact_list)) - 1
        contact_list.pop(user_answer)
        show_contacts(True)
        f = end_program(NumberText)
    save_contact()


def find_contact():
    global contact_list
    NumberText = '\n1 - Найти еще контакт \n0 - Выйти в главное меню \nВыберите операцию: '
    f = True
    while f:
        print('\nНайти номер по имени')
        user_input = input('Имя: ')
        user_find_list = []
        for i in contact_list:
            for key, value in i.items():
                if key == 'Name' and value == user_input:
                    user_find_list.append(i)
        if len(user_find_list) <= 0:
            print(f'Пользователей с именем {user_input} не найдено')
        else:
            for i in user_find_list:
                print(f'Пользователи с именем {user_input}')
                for key, value in i.items():
                    print(f'{key}: {value}', end=', ')
        f = end_program(NumberText)


def end_program(NumberText):
    print()
    userChoose = bool
    while True:
        if userChoose == 0:
            return False
        elif userChoose == 1:
            return True


def generate_random_string(length=8):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


def generate_random_phone_number(length=8, minNumber=0, maxNumber=9):
    result = '+'
    for i in range(length):
        result += str(random.randint(minNumber, maxNumber))
    return result
