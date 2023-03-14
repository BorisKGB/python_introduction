# 2.1[10]: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
# Количество монет и их положение (0 или 1) пользователь вводит с клавиатуры.
#
#     Примеры/Тесты:
#     Введите кол-во монет>? 5
#     Положение монеты 0: 0 или 1>? 1
#     ...
#     1 0 1 1 0
#     Кол-во монет, чтобы перевернуть: 2

import random

# user_input = input("Введите число монеток > ")
# if user_input.isdigit():
#     coins = int(user_input)
# else:
#     print("Вы ввели что-то не то, перезапустите программу и попробуйте ещё раз")
#     exit(1)
coins = 5

head = 0
tail = 1

head_coins = 0
tail_coins = 0

for i in range(1, coins+1):
    # спрашиваем пользователя
    # while True:
        # user_input = input(f"Положение монеты {i}: ")
        # if user_input.isdigit() and user_input in "01":
        #     coin = int(user_input)
        #     break
        # print("У монетки нет такой стороны, допускаются значения 0 или 1")
    # или генерируем значения и выводим их для отладки
    coin = random.randint(0, 1)
    print(coin, end=' ')
    #
    head_coins += 1 if coin == head else 0
    tail_coins += 1 if coin == tail else 0

print()
print(f'Кол-во монет, чтобы перевернуть: {head_coins if head_coins < tail_coins else tail_coins}')
