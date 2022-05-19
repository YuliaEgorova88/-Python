# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#    Входные и выходные данные хранятся в отдельных текстовых файлах.


# my_file = open('income_file.txt', 'w')
# my_file.write('AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE')


file = open('income_file.txt', 'r')
content = file.read()
print(content)
new = ''
cout = 1
for i in range(len(content) - 1):
    if i <= len(content):
        if content[i] == content[i + 1]:
            cout += 1
        else:
            a = content[i]
            new += str(cout) + content[i]
            cout = 1
new += str(cout) + content[i]
print(new)
file.close()
new_file = open('outcome_file.txt', 'w')
new_file.write(new)
new_file.close()
