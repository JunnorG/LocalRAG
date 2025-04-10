from text_utils.ChunkBase import ChunkBase
import fitz  # PyMuPDF
import nltk

class PdfFileToChunk(ChunkBase):
    def __init__(self):
        nltk.download('punkt_tab')
        self.chunk_size = 300

    def file_to_text(self, file_path):
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text

    def text_to_chunk(self, text):
        sentences = nltk.sent_tokenize(text)
        chunks = []
        current_chunk = []
        current_length = 0

        for sentence in sentences:
            sentence_length = len(sentence.split())
            if current_length + sentence_length <= self.chunk_size:
                current_chunk.append(sentence)
                current_length += sentence_length
            else:
                chunks.append(' '.join(current_chunk))
                current_chunk = [sentence]
                current_length = sentence_length

        if current_chunk:
            chunks.append(' '.join(current_chunk))

        return chunks