# 1.4[8]. Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 	Примеры/Тесты:
# 	3 2 4 -> yes
# 	3 2 1 -> no

print("Шоколадка размером MxN")
width_input = input("Введите M > ")
height_input = input("Введите N > ")
wanted_input = input("Введите cколько долек отломить > ")

if width_input.isdigit() and height_input.isdigit() and wanted_input.isdigit():
    width = int(width_input)
    height = int(height_input)
    wanted = int(wanted_input)
else:
    print("Вы ввели что-то не то, все значения должны быть числами, перезапустите программу и попробуйте ещё раз")
    exit(1)

# 1) отламываем меньше чем у нас есть
# 2) отламываем количество кратное одной из сторон
if wanted < width * height and (wanted % height == 0 or wanted % width == 0):
    print('yes')
else:
    print('no')
