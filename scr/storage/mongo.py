from pymongo import MongoClient
from bson.objectid import ObjectId


class MongoDB:
    def __init__(self, uri: str):
        self._uri = uri

    def insert_documents(
        self,
        documents: list,
        database: str,
        collection: str
    ):
        client = MongoClient(self._uri)
        coll = client[database][collection]

        if len(documents) > 1:
            coll.insert_many(documents).inserted_ids
        elif len(documents) == 1:
            coll.insert_one(documents[0]).inserted_id

    def get_documents(
        self,
        flag: str,
        database: str,
        collection: str
    ):
        client = MongoClient(self._uri)
        coll = client[database][collection]

        cursor = coll.find(
            {
                flag: {
                    "$exists": False
                }
            }
        )

        return list(cursor)

    def update_documents(
        self,
        ids: list[ObjectId],
        flag: str,
        database: str,
        collection: str
    ):
        client = MongoClient(self._uri)
        coll = client[database][collection]

        coll.update_many(
            {
                "_id": {
                    "$in": ids
                }
            }, {
                "$set": {
                    flag: True
                }
            }
        )
