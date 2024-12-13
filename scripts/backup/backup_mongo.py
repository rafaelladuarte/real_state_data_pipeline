from scripts.infra.security.secrets import get_secret_value

from pymongo import MongoClient
import json

client = MongoClient(get_secret_value("MONGO_URI"))
db = client["real_state"]


def export_collections_to_json(db):
    for collection_name in db.list_collection_names():
        collection = db[collection_name]
        data = list(collection.find())

        with open(f"scripts/backup/{collection_name}.json", "w") as json_file:
            json.dump(data, json_file, default=str, indent=4)
        print(f"Coleção {collection_name} exportada")


export_collections_to_json(db)
