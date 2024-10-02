from abc import ABC, abstractmethod

class SBlock(ABC):
    @abstractmethod
    def frw_S(self, blockIn: str, keyIn: str, jIn: int) -> str:
        pass

    @abstractmethod
    def inv_S(self, blockIn: str, keyIn: str, jIn: int) -> str:
        pass
