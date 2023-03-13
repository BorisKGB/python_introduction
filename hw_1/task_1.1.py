# 1.1[2]. Найдите сумму цифр трехзначного числа. Используйте f-строки чтобы оформить красивый вывод
#
# Например для числа 145 сумма цифр будет 10: 1 + 4 + 5
#
# 	Примеры/Тесты:
# 	123 >>> Сумма чисел числа 123 равна 6
# 	100 >>> Сумма чисел числа 100 равна 1

user_input = input("Введите трёхзначное число > ")
if len(user_input) == 3 and user_input.isdigit():
    input_number = int(user_input)
else:
    print("Вы ввели что-то не то, перезапустите программу и попробуйте ещё раз")
    exit(1)

number_digits_sum = 0

while input_number > 0:
    number_digits_sum += input_number % 10
    input_number //= 10

print(f'Сумма чисел числа {user_input} равна {number_digits_sum}')
