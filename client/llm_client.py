from abc import ABC, abstractmethod

class LLMClient(ABC):

    def __init__(self):
        self.connect()
        pass

    @abstractmethod
    def get_embedding(self):
        pass

    @abstractmethod
    def get_chat_completion(self):
        pass

    @abstractmethod
    def output_chat_completion_with_stream(self):
        pass