class HomeWork_One:
    import array

    mass = [1, 1, 2, 3, 5, 8, 13]
    # разворачиваем массив командой reverse

    mass.reverse()
    print(mass)

    i = 0
    newMassive = [None] * len(mass)
    print(newMassive)

    # разворачиваем массив циклом
    while i < len(mass):
        i += 1
        print(mass[len(mass) - i])


class HomeWork_Two:
    mass = [1, 1, 2, 3, 5, 8, 13]

    i = 0
    numbersBetween = 0
    minimum = 0
    maximum = 0
    minIndex = None
    maxIndex = None

    for elem in mass:
        if elem > maximum:
            maximum = elem
        if minimum == 0:
            minimum = elem
        if elem < minimum:
            minimum = elem

    minIndex = mass.index(minimum)
    maxIndex = mass.index(maximum)

    print("index of minimum", minIndex)
    print("index of maximum", maxIndex)
    print("Minumum: ", minimum)
    print("Maximum: ", maximum)

    i = minIndex

    while i < maxIndex:
        numbersBetween += mass[i]
        i += 1

    print("Summ of numbers between", numbersBetween)

    numbersBetween = 0

    for elem in mass:
        numbersBetween += elem

    print("Summ of all numbers", numbersBetween)
    numbersBetween = numbersBetween / len(mass)
    print("Arithmetic mean", int(numbersBetween))