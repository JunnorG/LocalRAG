import asyncio
from store.sqlite import Sqlite
from client.openai_client import OpenAIClient
from text_utils.PdfFileToChunk import PdfFileToChunk


def main(file_path, sql_db_path):
    # Step 1: Authenticate with Azure OpenAI using a token obtained via `az login`
    client = OpenAIClient()

    # Step 2: Parse the PDF document
    chunk_util = PdfFileToChunk()
    text = chunk_util.file_to_text(file_path)

    # Step 3: Split the parsed document into reasonable chunks
    chunks = chunk_util.text_to_chunk(text)

    # Step 4: Translate each chunk into a vector using an LLM model
    items = []
    for chunk in chunks:
        vector = client.get_embedding(chunk)
        items.append((chunk, vector))

    # Step 5: Store the vectors in a local store
    database = Sqlite(sql_db_path)
    database.connect()
    database.write_multiple_data(items)

    for data in database.read_all_data():
        print(data)

main('D:\个人资料\Resume_Weiqi Yuan.pdf', 'rag.db')
