from abc import ABC, abstractmethod


class BaseHomework(ABC):
    @abstractmethod
    def run(self):
        pass

# Example 1

# k = "член"

# setLetters = [
#     {"A", "E", "I", "O", "U", "L", "N", "S", "T", "R"},
#     {"D", "G"},
#     {"B", "C", "M", "P"},
#     {"F", "H", "V", "W", "Y"},
#     {"K"},
#     {"J", "X"},
#     {"Q", "Z"},
#     {"А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"},
#     {"Д", "К", "Л", "М", "П", "У"},
#     {"Б", "Г", "Ё", "Ь", "Я"},
#     {"Й", "Ы"},
#     {"Ж", "З", "Х", "Ц", "Ч"},
#     {"Ш", "Э", "Ю"},
#     {"Ф", "Щ", "Ъ"},
# ]
# setValues = [1, 2, 3, 4, 5, 8, 10, 1, 2, 3, 4, 5, 8, 10]

# result = 0
# listOfDictionaries = []

# for i in range(len(setValues)):
#     listOfDictionaries.append(dict.fromkeys(setLetters[i], setValues[i]))

# for let in k:
#     for i in range(len(listOfDictionaries)):
#         if let.upper() in listOfDictionaries[i]:
#             result += listOfDictionaries[i][let.upper()]

# print(result)