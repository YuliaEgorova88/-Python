import end_program


def find_employee(employee_list):
    NumberText = '\n1 - Найти еще контакт \n0 - Выйти в главное меню \nВыберите операцию: '
    f = True
    while f:
        print('\nНайти номер по имени')
        user_input = input('Имя: ')
        user_find_list = []
        for i in employee_list:
            for key, value in i.items():
                if key == 'Name' and value == user_input:
                    user_find_list.append(i)
        if len(user_find_list) <= 0:
            print(f'Пользователей с именем {user_input} не найдено')
        else:
            for i in user_find_list:
                print(f'Пользоватей с именем {user_input} найдено {len(user_find_list)}')
                for key, value in i.items():
                    print(f'{key}: {value}', end=', ')
        f = end_program(NumberText)
