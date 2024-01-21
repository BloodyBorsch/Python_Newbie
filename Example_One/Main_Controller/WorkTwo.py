from BaseWork import BaseHomework
from abc import ABC, abstractmethod


class HomeworkTwo(BaseHomework):
    def __init__(self):
        pass

    def run(self):
        print(f"Testing 2")
        
# # Напишите функцию print_operation_table(operation, num_rows, num_columns),
# # которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# # По умолчанию номер столбца и строки = 9.

# # Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.

# # Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).

# # Если строк меньше двух, выдайте текст
# # ОШИБКА! Размерности таблицы должны быть больше 2!.

# # Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

# # Между элементами должен быть 1 пробел, в конце строки пробел не нужен.

# # print_operation_table(lambda x, y: x * y, 3, 3)

# # 1 2 3
# # 2 4 6
# # 3 6 9

# # def same_by(characteristics, object):
# #     result = True
# #     list1 = [characteristics(x) for x in object]
# #     for i in range(len(list1) - 1):
# #         if list1[i] != list1[i + 1]:
# #             result = False
# #     return result


# # values = [0, 3, 10, 6]
# # if same_by(lambda x: x % 2, values):
# #     print("same")
# # else:
# #     print("different")

# list_one = [i + 1 for i in range(num_columns)]
# list_one = list(map(num_raise, range(num_columns)))
# columns = list(map(lambda x: x + 1, range(num_columns)))
# numbers_list.append(list(map(lambda x: x + 1, range(num_columns))))
# print(*numbers_list[0])

# numbers_list = list()


# def print_operation_table(operation, num_rows = 9, num_columns = 9):
#     if num_rows < 2:
#         return print(f"ОШИБКА! Размерности таблицы должны быть больше 2!")
#     for n in range(num_rows):
#         numbers_list.append([operation(n + 1, i + 1) for i in range(num_columns)])
#         print(*numbers_list[n])


# print_operation_table(lambda x, y: x * y)
