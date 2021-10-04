from abc import ABC, abstractmethod

class Step(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def process(self,data,inputs):
        pass

class StepException(Exception):  # Exception內建
    pass
