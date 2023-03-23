# 5.1[26]: Напишите рекурсивную функцию для возведения числа a в степень b.
# Разрешается использовать только операцию умножения. Циклы использовать нельзя
#
#     Примеры/Тесты:
#     <function_name>(2,0) -> 1
#     <function_name>(2,1) -> 2
#     <function_name>(2,3) -> 8
#     <function_name>(2,4) -> 16

def custom_pow(num: int, pow: int) -> int:
    if pow == 0: return 1
    return custom_pow(num, pow-1) * num


print(custom_pow(2, 0))
print(custom_pow(2, 1))
print(custom_pow(2, 3))
print(custom_pow(2, 4))
