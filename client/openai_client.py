from client.llm_client import LLMClient
from openai import AzureOpenAI


class OpenAIClient(LLMClient):
    def __init__(self):
        self.embedding_model = 'text-embedding-ada-002'
        self.chat_model = 'gpt-4-32k'
        # todo: set correct endpoint
        self.endpoint = '<--azure openai endpoint-->'
        self.api_version = '2024-12-01-preview'
        # todo: set correct key
        self.api_key = '<--azure openai api-key-->'
        self.client = AzureOpenAI(
            api_version=self.api_version,
            azure_endpoint=self.endpoint,
            api_key=self.api_key
        )

    def get_embedding(self, chunk):
        response = self.client.embeddings.create(input=chunk, model=self.embedding_model)
        vector = response.data[0].embedding
        return vector

    def get_chat_completion(self, prompt):
        response = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=1.0,
            top_p=1.0,
            model="gpt-4-32k"
        )
        return response.choices[0].message.content

    def output_chat_completion_with_stream(self, prompt):
        response = self.client.chat.completions.create(
            stream=True,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant.",
                },
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=1.0,
            top_p=1.0,
            model="gpt-4-32k"
        )
        for update in response:
            if update.choices:
                print(update.choices[0].delta.content or "", end="")
