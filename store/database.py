from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def close(self):
        pass
    @abstractmethod
    def write_multiple_data(self, items):
        pass
    @abstractmethod
    def read_all_data(self):
        pass