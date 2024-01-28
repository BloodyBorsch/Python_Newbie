from enum import Enum
import re

path_to_first = "data_first_variant.csv"
path_to_second = "data_second_variant.csv"


def input_data(new_data=True):
    print("Можно ввести * чтобы оставить поле без изменений")

    name = create_data(Data_types.first_name)
    surname = create_data(Data_types.second_name)
    phone = create_data(Data_types.phone_number)
    adress = create_data(Data_types.adress)
    account = dict(
        {
            Data_types.first_name: name,
            Data_types.second_name: surname,
            Data_types.phone_number: phone,
            Data_types.adress: adress,
        }
    )

    if new_data:
        var = int(
            input(
                f"В каком формате записать данные \n\n"
                f"1 Вариант: \n"
                f"{name}\n{surname}\n{phone}\n{adress}\n\n"
                f"2 Вариант: \n"
                f"{name}; {surname}; {phone}; {adress}\n"
                f"Выберите вариант: "
            )
        )

        data_variant(var, account)
    else:
        return account


def print_data():
    print(f"Вывожу данные из 1 файла: \n")
    with open(path_to_first, "r", encoding="utf-8") as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == "\n" or i == len(data_first) - 1:
                data_first_list.append(" ".join(data_first[j : i + 1]))
                j = i
        print(" ".join(data_first_list))

    print(f"Вывожу данные из 2 файла: \n")
    with open(path_to_second, "r", encoding="utf-8") as f:
        data_second = f.readlines()
        print(*data_second)


def edit_data():
    data_choose = int(input("Выберите файл 1 или 2: "))

    match data_choose:
        case 1:
            edit_column_data()
        case 2:
            edit_rows_data()
        case _:
            print(f"Нет такого файла для редактирования\n" "Введите заново")
            edit_data()


def erase_data():
    data_choose = int(input("Выберите файл 1 или 2: "))

    match data_choose:
        case 1:
            with open(path_to_first, "w", encoding="utf-8") as f:
                f.close()
        case 2:
            with open(path_to_second, "w", encoding="utf-8") as f:
                f.close()
        case _:
            print(f"Нет такого файла для удаления\n" "Введите заново")
            erase_data()


def create_data(num):
    data = input(data_collector(num))
    if data == "*":
        return
    else:
        return data


def edit_column_data():
    number_find = False

    what_to_edit = input("Введите номер телефона абонента: ")

    with open(path_to_first, "r", encoding="utf-8") as f:
        data_first = f.readlines()
        data_first_list = list(data_first)

        data_empty_check(data_first_list)

        for i in range(len(data_first_list)):
            if what_to_edit in data_first_list[i]:
                number_find = True
                print(f"Меняем данные в: {data_first_list[i - 2 : i + 2]}")
                temp_dict = input_data(False)
                if temp_dict[Data_types.first_name] != None:
                    data_first_list[i - 2] = f"{temp_dict[Data_types.first_name]}\n"
                if temp_dict[Data_types.second_name] != None:
                    data_first_list[i - 1] = f"{temp_dict[Data_types.second_name]}\n"
                if temp_dict[Data_types.phone_number] != None:
                    data_first_list[i] = f"{temp_dict[Data_types.phone_number]}\n"
                if temp_dict[Data_types.adress] != None:
                    data_first_list[i + 1] = f"{temp_dict[Data_types.adress]}\n"

        if number_find:
            print(" ".join(data_first_list))
        else:
            print(f"Нет такого телефона!")
            edit_data()

    with open(path_to_first, "w", encoding="utf-8") as f:
        [f.write(data_first_list[i]) for i in range(len(data_first_list))]


def edit_rows_data():
    what_to_edit = input("Введите номер телефона абонента: ")

    with open(path_to_second, "r", encoding="utf-8") as f:
        data_second = f.readlines()
        data_second_list = list(data_second)

        data_empty_check(data_second_list)

        for i in range(len(data_second_list)):
            if what_to_edit in data_second_list[i]:
                print(f"Меняем данные в: {data_second_list[i]}")

                # temp_list = (data_second_list[i]).split(";")
                temp_list = re.split(";| |\n", data_second_list[i])
                [print(x) for x in temp_list]

                temp_dict = input_data(False)
                if temp_dict[Data_types.first_name] != None:
                    name = temp_dict[Data_types.first_name]
                else:
                    name = temp_list[0]
                if temp_dict[Data_types.second_name] != None:
                    surname = temp_dict[Data_types.second_name]
                else:
                    surname = temp_list[1]
                if temp_dict[Data_types.phone_number] != None:
                    phone = temp_dict[Data_types.phone_number]
                else:
                    phone = temp_list[2]
                if temp_dict[Data_types.adress] != None:
                    adress = temp_dict[Data_types.adress]
                else:
                    adress = temp_list[3]

                data_second_list[i] = f"{name}; {surname}; {phone}; {adress}"

    with open(path_to_second, "w", encoding="utf-8") as f:
        [f.write(data_second_list[i]) for i in range(len(data_second_list))]


def data_collector(Dtype):
    match Dtype:
        case Data_types.first_name:
            return f"Введите имя: "
        case Data_types.second_name:
            return f"Введите фамилию: "
        case Data_types.phone_number:
            return f"Введите телефон: "
        case Data_types.adress:
            return f"Введите адрес: "
        case _:
            print(f"Выход за пределы вводимых значений")


def data_variant(Dtype, account):
    match Dtype:
        case 1:
            with open(path_to_first, "a", encoding="utf-8") as f:
                f.write(
                    f"{account[Data_types.first_name]}\n{account[Data_types.second_name]}\n{account[Data_types.phone_number]}\n{account[Data_types.adress]}\n\n"
                )
                pass
        case 2:
            with open(path_to_second, "a", encoding="utf-8") as f:
                f.write(
                    f"{account[Data_types.first_name]}; {account[Data_types.second_name]}; {account[Data_types.phone_number]}; {account[Data_types.adress]}\n\n"
                )
        case _:
            print(f"Число должно быть 1 либо 2")
            data_variant((int(input(f"Введите число: "))), account)


def data_empty_check(test_list):
    if len(test_list) < 1:
        print(f"Файл пустой")
        return edit_data()


class Data_types(Enum):
    first_name = 1
    second_name = 2
    phone_number = 3
    adress = 4
