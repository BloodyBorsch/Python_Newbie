# list_one = [i + 1 for i in range(num_columns)]
# list_one = list(map(num_raise, range(num_columns)))
# columns = list(map(lambda x: x + 1, range(num_columns)))
# numbers_list.append(list(map(lambda x: x + 1, range(num_columns))))
# print(*numbers_list[0])

numbers_list = list()


def print_operation_table(operation, num_rows = 9, num_columns = 9):
    if num_rows < 2:
        return print(f"ОШИБКА! Размерности таблицы должны быть больше 2!")
    for n in range(num_rows):
        numbers_list.append([operation(n + 1, i + 1) for i in range(num_columns)])
        print(*numbers_list[n])


print_operation_table(lambda x, y: x * y)
