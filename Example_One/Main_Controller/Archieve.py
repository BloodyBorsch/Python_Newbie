# vowels = ("а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е")
# result = bool()
# vowels_list = list()
# stroka = "пара-ра-Рам рам-Пам-папам Па-ра-па-дам"

# stroka_list = stroka.split()
# stroka_list = list(map(lambda x: x.lower(), stroka_list))


# def Calculation():
#     result = True

#     if len(stroka_list) <= 1:
#         return print(f"Количество фраз должно быть больше одной!")

#     for i in stroka_list:
#         vowels_list.append(list(filter(lambda x: x in vowels, i)))

#     print(stroka_list)
#     print(vowels_list)

#     for i in vowels_list:
#         if len(i) != len(vowels_list[0]):
#             result = False
#             break

#     if result:
#         return print(f"Парам пам-пам")
#     else:
#         return print(f"Пам парам")


# Calculation()

# # # # # # # # # # # # # # # # # # # # # 

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

# # # # # # # # # # # # # # # # # # # # # # # # # # # 

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

