# 1.2[4]. Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали ```S``` журавликов.
# Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#
# 	Примеры/Тесты:
# 	6 >>>  1  4  1
# 	24 >>> 4  16  4
# 	60 >>> 10  40  10

user_input = input("Введите количество сделанных журавликов > ")
if not user_input.isdigit():
    print("Вы ввели что-то не то, перезапустите программу и попробуйте ещё раз")
    exit(1)
number = int(user_input)

# Петя
user1_efficiency = 1
# Катя
user2_efficiency = 4
# Серёжа
user3_efficiency = 1

users_efficiency = user1_efficiency + user2_efficiency + user3_efficiency

if number % users_efficiency == 0:
    part = number // users_efficiency
    # print("Петя сделал", user1_efficiency * part, "журавликов")
    # print("Катя сделала", user2_efficiency * part, "журавликов")
    # print("Серёжа сделал", user3_efficiency * part, "журавликов")
    # или в формате, как требуется задачей
    print(user1_efficiency * part, user2_efficiency * part, user3_efficiency * part, sep='  ')
else:
    print("Нет возможности посчитать, число не делится без остатка. Значит кто-то не доделал своих журавликов")
