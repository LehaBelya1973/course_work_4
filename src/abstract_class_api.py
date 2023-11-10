from abc import ABC, abstractmethod


class WorkWithAbstract(ABC):
    @abstractmethod
    def request(self):
        pass
