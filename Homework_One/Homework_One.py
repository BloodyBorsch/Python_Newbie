class HomeWork_One:
    import array

    mass = [1, 1, 2, 3, 5, 8, 13]
    # reversing of massive by using Reverse command

    mass.reverse()
    print(mass)

    i = 0
    newMassive = [None] * len(mass)
    print(newMassive)

    # reversing massive vith cycle
    while i < len(mass):
        i += 1
        newMassive[i - 1] = mass[len(mass) - i]
        
    mass = newMassive
    print(mass)


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

class HomeWork_Three:
    
    numbers = [2, 5, 13, 7, 6, 4]
    size = 0
    summ = 0
    avg = 0
    index = 0
    
    size = len(numbers)
    while index < size:
        summ += numbers[index]
        index += 1
    
    avg = summ/size
    print(int(avg))