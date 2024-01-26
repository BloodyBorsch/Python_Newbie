from enum import Enum

path_to_first = "data_first_variant.csv"
path_to_second = "data_second_variant.csv"


def input_data():
    name = create_data(Data_types.firstname)
    surname = create_data(Data_types.surname)
    phone = create_data(Data_types.phone_number)
    adress = create_data(Data_types.adress)

    var = int(
        input(
            f"В каком формате записать данные \n\n"
            f"1 Вариант: \n"
            f"{name}\n{surname}\n{phone}\n{adress}\n\n"
            f"2 Вариант: \n"
            f"{name};{surname};{phone};{adress}\n"
            f"Выберите вариант: "
        )
    )

    data_variant(var, name, surname, phone, adress)


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
    print(f"Edit")


def erase_data():
    print(f"Erase")


def create_data(num):
    data = input(data_collector(num))
    return data


def data_collector(Dtype):
    match Dtype:
        case Data_types.firstname:
            return f"Введите имя: "
        case Data_types.surname:
            return f"Введите фамилию: "
        case Data_types.phone_number:
            return f"Введите телефон: "
        case Data_types.adress:
            return f"Введите адрес: "
        case _:
            print(f"Выход за пределы вводимых значений")


def data_variant(Dtype, name, surname, phone, adress):
    match Dtype:
        case 1:
            with open(path_to_first, "a", encoding="utf-8") as f:
                f.write(f"{name}\n{surname}\n{phone}\n{adress}\n\n")
        case 2:
            with open(path_to_second, "a", encoding="utf-8") as f:
                f.write(f"{name};{surname};{phone};{adress}\n\n")
        case _:
            print(f"Число должно быть 1 либо 2")
            data_variant((int(input(f"Введите число: "))), name, surname, phone, adress)


class Data_types(Enum):
    firstname = 1
    surname = 2
    phone_number = 3
    adress = 4
