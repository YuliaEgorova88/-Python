from Homework5.out import menu
from Homework5.prog.contact import add_contact, show_contacts, del_contact, find_contact, load_contacts
from Homework5.input import user_answer


def start():
    while True:
        load_contacts(False)
        menu.get_menu()
        user_select = user_answer.read_user_answer()
        if user_select == 0:
            print('GoodBye! See you later!')
            break
        elif user_select == 1:
            add_contact()
        elif user_select == 2:
            del_contact()
        elif user_select == 3:
            show_contacts()
        elif user_select == 4:
            find_contact()
