import end_program
import read_data, load_employees


def show_employee_list(flag=True):
    NumberText = '\n1 - Обновить список сотрудников \n0 - Выйти в главное меню \nВыберите операцию: '
    f = True
    flag2 = load_employees()
    if flag2:
        print('\nСписок сотрудников')
    if not flag:
        read_data()
    else:
        while f:
            read_data()
            f = end_program(NumberText)
