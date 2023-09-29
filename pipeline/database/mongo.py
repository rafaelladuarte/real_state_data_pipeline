from pymongo import MongoClient
import os


class Mongo:
    def __init__(self):
        cli = MongoClient(host=os.environ["MONGO_URI"])
        self.db = cli["olist_raw"]

    def list_collections(self) -> list:
        return self.db.list_collection_names()

    def get_data(self, collection: str) -> list[dict]:
        cursor = self.db[collection].find()
        documents = []

        for c in cursor:
            documents.append(c)

        return documents

    def post_data(self, collection: str, data: list[dict]) -> None:
        col = self.db[collection]
        inserted_ids = col.insert_many(data).inserted_ids
        print(f"Inseridos {len(inserted_ids)} documentos em '{collection}'")
