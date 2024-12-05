from bson.objectid import ObjectId
from pymongo import MongoClient


class MongoDB:
    def __init__(self, uri: str):
        self._uri = uri

    def insert_documents(
        self,
        documents: list,
        collection: str
    ):
        client = MongoClient(self._uri)
        coll = client["real_state"][collection]

        documents = [{**doc, '_id': ObjectId()} for doc in documents]

        if len(documents) > 1:
            coll.insert_many(documents)
        elif len(documents) == 1:
            coll.insert_one(documents[0])

    def get_documents(
        self,
        query: dict,
        collection: str
    ):
        client = MongoClient(self._uri)
        coll = client["real_state"][collection]

        cursor = coll.find(query)
        data = []
        for c in cursor:
            data.append(c)

        return data

    def update_documents(
        self,
        query: dict,
        set: dict,
        collection: str
    ):
        client = MongoClient(self._uri)
        coll = client["real_state"][collection]

        coll.update_many(query, set)

    def update_document(
        self,
        query: dict,
        set: dict,
        collection: str
    ):
        client = MongoClient(self._uri)
        coll = client["real_state"][collection]

        coll.update_one(query, set)

    def get_documents_aggregate(
        self,
        pipeline: list,
        collection: str
    ):
        client = MongoClient(self._uri)
        coll = client["real_state"][collection]

        cursor = coll.aggregate(pipeline)

        data = []
        for c in cursor:
            data.append(c)

        return data

    def find_missing_mobi_url(
        self,
        list_url: list,
    ) -> list:
        client = MongoClient(self._uri)
        coll = client['real_state']['imobiliarias']

        existing_mobi_url = coll.distinct(
            "id_imobiliaria",
            {
                "imobiliaria": {
                    "$in": list_url
                }
            }
        )

        missing_mobi_url = [
            mobi_id
            for mobi_id in list_url
            if mobi_id not in existing_mobi_url
        ]

        return missing_mobi_url

    def get_ids_uniques(
            self,
            flag: str,
            collection: str
    ) -> list:
        client = MongoClient(self._uri)
        coll = client['real_state'][collection]

        cursor = coll.distinct(key=flag)
        data = cursor[:50]

        client.close()

        return data

    def list_collection_names(self):
        client = MongoClient(self._uri)
        database = client['real_state']

        data = database.list_collection_names()

        return data
