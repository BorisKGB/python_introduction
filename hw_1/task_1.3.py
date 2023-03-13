# 1.3[6]. Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
#
# 	Примеры/Тесты:
# 	385916 >>> yes
# 	123456 >>> no

ticket_size = 6
user_input = input("Введите номер билета > ")
if len(user_input) == ticket_size and user_input.isdigit():
    ticket_number = int(user_input)
else:
    print("Это не номер билета, перезапустите программу и попробуйте ещё раз")
    exit(1)

sum_left = 0
sum_right = 0

while ticket_number > 0:
    sum_right += ticket_number % 10
    ticket_number //= 10
    ticket_size -= 1
    sum_left += ticket_number // 10**(ticket_size-1)
    ticket_number %= 10**(ticket_size-1)
    ticket_size -= 1

if sum_left == sum_right:
    print("yes")
else:
    print("no")
