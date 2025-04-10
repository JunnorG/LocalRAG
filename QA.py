from client.openai_client import OpenAIClient
from store.sqlite import Sqlite

prompt_template = """  
1. Use ONLY the context below.  
2. If unsure, say "I don’t know".  
3. Keep answers under 4 sentences.  

Context: {context}  

Question: {question}  

Answer:  
"""
client = OpenAIClient()


def get_vector(client, chunk):
    return client.get_embedding(chunk)


def generate_answer(question):
    vector = get_vector(client, question)
    database = Sqlite("rag.db")

    similar_items = database.search_similar_items((question, vector))
    context = ""
    for item in similar_items:
        context = context + item[0] + '\n'
    prompt = prompt_template.replace('{context}', context).replace('{question}', question)
    #  prompt = "给我一份上海一日游的教程"
    client.output_chat_completion_with_stream(prompt)


generate_answer('今天天气怎么样')
