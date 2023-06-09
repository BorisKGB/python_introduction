# 3.1[16]: Дан список целых чисел.  Требуется вычислить, сколько раз встречается некоторое число X в этом списке.
# Пользователь вводит число X с клавиатуры. Список можно считать заданным.
# Если такого числа в списке нет - вывести -1.
#
# 	Примеры/Тесты:
#     Input:   [10, 5, 7, 3, 3, 0, 5, 7, 2, 8], x = 3
#     Output:  2
#
#     Input:   [10, 5, 7, 3, 3, 0, 5, 7, 2, 8], x = 20
#     Output:  -1
# Напишите алгоритм подсчета самостоятельно или воспользуйтесь методами списка.
#
# ```(*)``` **Усложнение.** При выводе результата на экран воспользуйтесь тернарным оператором.

numbers = [10, 5, 7, 3, 3, 0, 5, 7, 2, 8]

user_input = input("Введите число > ")
if user_input.isdigit():
    input_number = int(user_input)
else:
    print("Вы ввели что-то не то, перезапустите программу и попробуйте ещё раз")
    exit(1)

# метод списка
# print(numbers.count(input_number) if input_number in numbers else -1)

# своими силами
number_count = 0
for number in numbers:
    if number == input_number:
        number_count += 1

if number_count > 0:
    print(number_count)
else:
    print(-1)
