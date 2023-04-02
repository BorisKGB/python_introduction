# 6.2[32]: Напишите функцию ```print_operation_table(operation, num_rows=6, num_columns=6)```,
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца,
# т.е. функцию двух аргументов. Аргументы ```num_rows``` и ```num_columns``` указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы.
#
# 	Примеры/Тесты:
#     print_operation_table(lambda x,y: x**y,4,4)
# 	1   1   1   1
# 	2   4   8  16
# 	3   9  27  81
# 	4  16  64 256
#
#     print_operation_table(lambda x,y: x*y)
# 	1   2   3   4   5   6
# 	2   4   6   8  10  12
# 	3   6   9  12  15  18
# 	4   8  12  16  20  24
# 	5  10  15  20  25  30
# 	6  12  18  24  30  36
#
#
# ```(*)``` **Усложнение.** Сформируйте форматированный вывод с номерами строк и столбцов
#
# 	Примеры/Тесты:
# 	print_operation_table(lambda x,y: x**y,4,4)
# 	       1   2   3   4
# 	    ----------------
# 	1 |    1   1   1   1
# 	2 |    2   4   8  16
# 	3 |    3   9  27  81
# 	4 |    4  16  64 256
#
# 	print_operation_table(lambda x,y: x*y)
# 	       1   2   3   4   5   6
# 	    ------------------------
# 	1 |    1   2   3   4   5   6
# 	2 |    2   4   6   8  10  12
# 	3 |    3   6   9  12  15  18
# 	4 |    4   8  12  16  20  24
# 	5 |    5  10  15  20  25  30
# 	6 |    6  12  18  24  30  36

# first solution
# def print_operation_table(operation, num_rows=6, num_columns=6):
#     print(" "*3, *(f"{column:>4}" for column in range(1, num_columns+1)), sep='')
#     print(" "*3, "-"*4*num_columns, sep='')
#     [print(f"{row:<2}|", *(f"{operation(row, column):>4}"
#                            for column in range(1, num_columns + 1)), sep='') for row in range(1, num_rows + 1)]

# second solution
def approx_element_size(operation, num_rows, num_columns):
    """Trying to determine max needed symbols for one element, but check only corner elements"""
    if type(operation(1, 1)) is float:
        # if operation return float, then there may be output like (1/3)0.33333....
        # And most likely we do not found it on corners,
        # so just return whatever value auto conversion decides to use
        return len(str(1/3)) + 1  # -> 19 (at least on my PC)
        # it is probable make sense to just return 19, but i`m not sure if this is a preset value or not
    value_lens = (len(str(operation(row, column))) for row in (1, num_rows) for column in (1, num_columns))
    # points = [(row, column) for row in (1, num_rows) for column in (1, num_columns)]  # for debug
    return max(value_lens) + 1


def print_operation_table(operation, num_rows=6, num_columns=6):
    row_number_element_size = len(str(num_rows)) + 1
    # try to calculate element size
    element_size = approx_element_size(operation, num_rows, num_columns)
    # header
    print(" " * (row_number_element_size + 1),
          *("{0:>{width}}".format(column, width=element_size) for column in range(1, num_columns + 1)), sep='')
    print(" " * (row_number_element_size + 1), "-" * element_size * num_columns, sep='')
    # main table with row_numbers
    [print("{0:<{width}}|".format(row, width=row_number_element_size),
           *("{0:>{width}}".format(operation(row, column), width=element_size)
             for column in range(1, num_columns + 1)), sep='') for row in range(1, num_rows + 1)]


print_operation_table(lambda x, y: x**y, num_rows=4, num_columns=4)
