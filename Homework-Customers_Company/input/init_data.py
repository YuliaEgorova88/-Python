import pickle

employee_list = []


def init():
    global employee_list
    load_employees(False)
    return employee_list


def load_employees(f=True):
    global employee_list
    path = 'employees.txt'
    try:
        with open(path, 'rb') as data:
            employee_list = pickle.load(data)
    except:
        if not f:
            print()
        else:
            print('Нет сотрудников!')
            return False
    return True


def read_data():
    global employee_list
    counter = 1
    print()
    for i in employee_list:
        print(f'{counter} - ', end='')
        for key, value in i.items():
            print(f'{key}: {value}', end=', ')
        print()
        counter += 1
    print(f'Обшее количество сотрудников {len(employee_list)}')
