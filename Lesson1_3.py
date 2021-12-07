#3. Узнайте у пользователя число n. #Найдите сумму чисел n + nn + nnn. #Например, пользователь ввёл число #3. Считаем 3 + 33 + 333 = 369.

n = int(input('Введите число: '))
result = str(n)
num1 = result + result
num2 = result + result + result
total = n + int(num1) + int(num2)
print(total)