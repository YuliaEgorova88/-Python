from .show import show_employee_list
# import save
# import end_program


def delete_employee(employee_list):
    NumberText = '\n1 - Удалить еще сотрудника \n0 - Выйти в главное меню \nВыберите операцию: '
    read_user_answer_text = 'Выберите кого хотите удалить по цифре: '
    show_employee_list(False)
    f = True
    while f:
        user_choose = read_user_answer_text(read_user_answer_text, minNumber=1, maxNumber=len(employee_list)) - 1
        employee_list.pop(user_choose)
        save(employee_list)
        show_employee_list(False)
        f = end_program(NumberText)
    print()
