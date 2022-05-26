# import end_program
# import save


def add_employee(employee_list):
    NumberText = '\n1 - Добавить еще сотрудника \n0 - Выйти в главное меню \nВыберите операцию: '
    f = True
    while f:
        employee_list.append({'Name': input('Имя: '), 'SurName': input('Фамилия: '), 'Position': input('Должность: '), 'Salary': input('Зарплата: ')})
        f = end_program(NumberText)
    save(employee_list)
    print()