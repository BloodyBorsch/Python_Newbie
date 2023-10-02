from abc import ABC, abstractmethod


class BaseHomework(ABC):
    @abstractmethod
    def run(self):
        pass
