# 6.1[30]: Напишите программу, генерирующую элементы арифметической прогрессии
# Программа принимает от пользователя три числа :
#
# - Первый элемент прогрессии, Разность (шаг) и Количество элементов
#
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
#
# 	Напишите функцию
#
# 	- Аргументы: три указанных параметра
# 	- Возвращает: список элементов арифмитической прогрессии.
#
# 	Примеры/Тесты:
#
# 	Ввод: 7 2 5
# 	Вывод: [7 9 11 13 15]
# 	Ввод: 2 3 12
# 	Вывод: [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
#
# ```(*)``` **Усложнение.** Для формирования списка внутри функции используйте Comprehension
#
# ```(**)``` **Усложнение.** Присвоение значений переменным a1,d,n запишите,
# используя только один input, в одну строку, вам понадобится распаковка и Comprehension или map

def sequence_elements(start_element: int, step: int, max_elements: int) -> list:
    return [start_element + (x-1) * step for x in range(1, max_elements+1)]


greeting_string = "Введите числа через пробел ('первый элемент прогрессии' 'шаг' 'количество элементов' > "
# data input methods, pick one
# using map
a1, d, n = map(int, input(greeting_string).split())
# using comprehension and unpacking
#  a1, d, n = [int(elem) for elem in input(greeting_string).split()]
# preset data
#  a1, d, n = 7, 2, 5

print(sequence_elements(a1, d, n))
