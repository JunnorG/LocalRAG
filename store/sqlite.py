import json
import sqlite3

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from store.database import Database

class Sqlite(Database):

    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)

    def connect(self):
        pass

    def close(self):
        self.conn.close()

    def write_multiple_data(self, items):
        c = self.conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS vectors (
                id INTEGER PRIMARY KEY, 
                content TEXT, 
                vector JSON
                )
            ''')
        for item in items:
            c.execute("INSERT INTO vectors (content, vector) VALUES (?, ?)", (item[0], json.dumps(item[1])))
        self.conn.commit()

    def read_all_data(self):
        cursor = self.conn.cursor()

        cursor.execute('SELECT * FROM vectors')
        rows = cursor.fetchall()
        results = []
        for row in rows:
            results.append((row[1], json.loads(row[2])))
        self.conn.close()
        return results

    # item: (content, vector)

    def search_similar_items(self, compared_item, top_n=5, similarity_threshold=0.5, db_path="vectors.db"):
        all_items = self.read_all_data()
        vectors = np.array([item[1] for item in all_items])
        compared_vector = np.array(compared_item[1]).reshape(1, -1)

        cosine_similarities = cosine_similarity(compared_vector, vectors)
        cosine_similarities_arr = cosine_similarities.tolist()[0]
        # 获取相似度最高的前N段文本
        similar_indices = cosine_similarities.argsort()[-top_n:]
        similar_indices_arr = similar_indices.tolist()[0]

        similar_items = []
        for i in similar_indices_arr:
            if (cosine_similarities_arr[i] > similarity_threshold):
                similar_items.append((all_items[i]))

        return similar_items

# database = Sqlite("temp.db")
# database.connect()
# items = [
#     ("first chunk", [0.1, 0.2]),
#     ("second chunk", [0.3, 0.4])
# ]
# database.write_multiple_data(items)
# print(database.read_all_data())
# database.close()
