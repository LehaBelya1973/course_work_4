from abc import ABC, abstractmethod


class WorkWithAbstract(ABC):
    """Запрос общий на все сайты"""

    @abstractmethod
    def request(self):
        pass
