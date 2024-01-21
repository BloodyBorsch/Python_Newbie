vowels = ("а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е")
result = bool()
vowels_list = list()
# stroka = "пара-ра-Рам рам-Пам-папам Па-ра-па-дам"
# stroka = "пара-ра-Рам"
stroka = "по-русски говорят"
stroka_list = stroka.split()
stroka_list = list(map(lambda x: x.lower(), stroka_list))


def Calculation():
    result = True

    if len(stroka_list) <= 1:
        return print(f"Количество фраз должно быть больше одной!")

    for i in stroka_list:
        vowels_list.append(list(filter(lambda x: x in vowels, i)))

    print(stroka_list)
    print(vowels_list)

    for i in vowels_list:
        if len(i) != len(vowels_list[0]):
            result = False
            break

    if result:
        return print(f"Парам пам-пам")
    else:
        return print(f"Пам парам")


Calculation()