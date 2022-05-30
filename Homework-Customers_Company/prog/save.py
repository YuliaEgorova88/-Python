import pickle


def save_employee(employee_list):
    path = 'employees.txt'
    try:
        with open(path, 'wb') as data:
            pickle.dump(employee_list, data)
    except:
        print('Ошибка при записи сотрудников в файл')
