# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#    Входные и выходные данные хранятся в отдельных текстовых файлах.


#my_file = 'AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE'
with open('income_file.txt', 'w') as my_file:
    my_file.write('AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE')
    cout = 1
    for i in range(len(my_file)):
        if i <= len(my_file):
            if my_file[i] == my_file[i + 1]:
                cout += 1
            else:
                a = my_file[i]
                print(cout, my_file[i])
                cout = 1

with open('outcome_file.txt', 'w') as my_new_file:
    my_new_file.write(str(cout) + my_file[i])
#print(str(cout) + my_file[i])
