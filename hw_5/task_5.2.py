# 5.2[28]: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Циклы использовать нельзя
#
# 	Примеры/Тесты:
#     <function_name>(0,0) -> 0
#     <function_name>(0,2) -> 2
#     <function_name>(3,0) -> 3

def custom_sum(first_num: int, second_num: int) -> int:
    if second_num == 0: return first_num
    return custom_sum(first_num+1, second_num-1)


print(custom_sum(0, 0))
print(custom_sum(0, 2))
print(custom_sum(3, 0))
