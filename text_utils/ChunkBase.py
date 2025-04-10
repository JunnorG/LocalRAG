from abc import abstractmethod


class ChunkBase:
    @abstractmethod
    def file_to_text(self, file_path):
        pass

    @abstractmethod
    def text_to_chunk(self, text):
        pass
