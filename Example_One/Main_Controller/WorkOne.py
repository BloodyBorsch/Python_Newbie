from BaseWork import BaseHomework
from abc import ABC, abstractmethod


class HomeworkOne(BaseHomework):
    def __init__(self):
        pass

    def run(self):
        print(f"Testing 1")
        
        s = 11
        p = 30

        firstNum = s
        secondNum = 0

        while p % firstNum != 0 and ((firstNum + secondNum) != s):
            firstNum -= 1
            secondNum = int(p / firstNum)

        if ((firstNum + secondNum) == s):
            print(firstNum, secondNum)