# import WorkOne, WorkTwo, WorkThree, WorkFour, WorkFive
from WorkOne import HomeworkOne as work_one
from WorkTwo import HomeworkTwo as work_two
from WorkThree import HomeworkThree as work_three
from WorkFour import HomeworkFour as work_four
from WorkFive import HomeworkFive as work_five
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
                work_one.run(self)
            case WorkType.secondWork:
                work_two.run(self)
            case WorkType.thirdWork:
                work_three.run(self)
            case WorkType.fourthWork:
                work_four.run(self)
            case WorkType.fifthWork:
                work_five.run(self)


CHOOSE_HOMEWORK_TO_RUN = 1  # Домашку выбирать тут, от 1 до 5

controller = MainController()
controller.run(WorkType(CHOOSE_HOMEWORK_TO_RUN))
