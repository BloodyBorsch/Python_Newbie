import WorkOne, WorkTwo, WorkThree, WorkFour, WorkFive
from enum import Enum


class WorkType(Enum):
    firstWork = 1
    secondWork = 2
    thirdWork = 3
    fourthWork = 4
    fifthWork = 5


class MainController:
    def run(self, work):
        match work:
            case WorkType.firstWork:
                WorkOne.HomeworkOne.run(self)
            case WorkType.secondWork:
                WorkTwo.HomeworkTwo.run(self)
            case WorkType.thirdWork:
                WorkThree.HomeworkThree.run(self)                
            case WorkType.fourthWork:
                WorkFour.HomeworkFour.run(self)                
            case WorkType.fifthWork:
                WorkFive.HomeworkFive.run(self)
                

CHOOSE_HOMEWORK_TO_RUN = 5 # Домашку выбирать тут, от 1 до 5

controller = MainController()
controller.run(WorkType(CHOOSE_HOMEWORK_TO_RUN))
