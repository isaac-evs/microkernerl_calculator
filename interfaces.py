from abc import ABC, abstractmethod


class OperationPlugin(ABC):
    @property
    @abstractmethod
    def name(self):
        """symbol or name of the operation (e.g., '+')"""
        pass

    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        """calculation logic"""
        pass
