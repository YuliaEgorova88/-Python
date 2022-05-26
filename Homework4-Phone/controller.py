from out.menu import get_menu
from input import user_answer, init_data
from prog.add import add_employee
from prog.show import show_employee_list
from prog.delete import delete_employee
from prog.find_employee import find_employee


def start():
    while True:
        employee_list = init_data.init()
        get_menu()
        user_select = user_answer.read_user_answer()
        if user_select == 0:
            print('GoodBye! See you later!')
            break
        elif user_select == 1:
            add_employee.add_employee(employee_list)
        elif user_select == 2:
            show_employee_list.show_employee_list()
        elif user_select == 3:
            find_employee(employee_list)
        elif user_select == 4:
            delete_employee.delete_employee(employee_list)