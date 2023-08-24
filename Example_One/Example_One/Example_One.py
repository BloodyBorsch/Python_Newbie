# class LessonOne:

#     count = 0
#     firstFriendSpeed = 1
#     secondFriendSpeed = 2
#     dogSpeed = 5
#     distance = 0
#     minDistanceBetween = 10

#     def TimeCount(distance, speedOfFriend, speedOfDog):
#         distance/(speedOfFriend + speedOfDog)

#     def DistanceCheck(distanceBetween, minDistance):
#         return(bool(distanceBetween > minDistance))

#     print(DistanceCheck(distance, minDistanceBetween))

# class LessonTwo:

#     count = 0
#     factorial = int(input())
#     solution = 1

#     while count < factorial:
#         count += 1
#         solution *= count
#     else:
#         print(solution)

# class LessonThree:

#     massive = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#     for elem in massive:
#         if elem < 5:
#             print(elem)

#     print([elem for elem in massive if elem < 5])

import enum
import random


class BotStatus(enum.Enum):
    FindTarget = 4
    Inspection = 3
    Moving = 2
    Idle = 1


def move():
    return "moving"


def finding():
    return "finding"


def inspection():
    return "inspection"


def idle():
    return "do nothing"


botSwitcher = {
    BotStatus.FindTarget: finding,
    BotStatus.Inspection: inspection,
    BotStatus.Moving: move,
    BotStatus.Idle: idle,
}


def sendCommandBot(argument):
    status = botSwitcher.get(argument, "bad command")
    return status()


def getRandom():
    result = random.choice(list(BotStatus))
    print(result)
    return result

print(list(BotStatus))
print(sendCommandBot(getRandom()))

# for element in BotStatus:
#     print(element.name, element.value)