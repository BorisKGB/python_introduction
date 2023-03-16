# 3.2[18]: Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X.
# Пользователь вводит это число с клавиатуры, список можно считать заданным.
# Введенное число не обязательно содержится в списке.
#
#     Примеры/Тесты:
#     Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
#     Output: 2
#     Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9

numbers = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]

user_input = input("Введите число > ")
if user_input.isdigit():
    input_number = int(user_input)
else:
    print("Вы ввели что-то не то, перезапустите программу и попробуйте ещё раз")
    exit(1)

closest_number = numbers[0]
difference = abs(input_number - closest_number)


for number in numbers:
    if abs(input_number - number) < difference:
        closest_number = number
        difference = abs(input_number - number)

print(closest_number)
