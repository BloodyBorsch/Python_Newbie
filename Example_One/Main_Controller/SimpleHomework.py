numbers_list = list()


def print_operation_table(operation, num_rows, num_columns):
    # list_one = [i + 1 for i in range(num_columns)]
    # list_one = list(map(num_raise, range(num_columns)))
    # columns = list(map(lambda x: x + 1, range(num_columns)))
    numbers_list.append(list(map(lambda x: x + 1, range(num_columns))))
    print(*numbers_list[0])

    for n in range(num_rows - 1):
        numbers_list.append(
            [operation(n + 2, numbers_list[0][i]) for i in range(num_columns)]
        )
        print(*numbers_list[n + 1])


print_operation_table(lambda x, y: x * y, 6, 6)
