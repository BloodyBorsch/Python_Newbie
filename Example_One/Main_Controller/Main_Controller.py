from Functions import input_data, print_data, edit_data, erase_data, int_parser


def work_with_data(number):
    match number:
        case 1:
            input_data()
        case 2:
            print_data()
        case 3:
            edit_data()
        case 4:
            erase_data()
        case _:
            print(f"Число должно быть от 1 до 4")
            work_with_data(int(input(f"Введите число: ")))


def interface():
    print(
        f"Добрый день! Вас приветствует бот справочник."
        "\n 1 - Ввод данных "
        "\n 2 - Вывод данных "
        "\n 3 - Изменение данных "
        "\n 4 - Очистка данных "
    )
    command, go_next = int_parser(input(f"Введите число: "))

    if not go_next:
        print(command)
        interface()
        return

    work_with_data(command)


if __name__ == "__main__":
    interface()
