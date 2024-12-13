from scripts.infra.security.secrets import get_secret_value

from pymongo import MongoClient

import json
import os


client = MongoClient(get_secret_value('MONGO_URI'))
db = client["real_state"]


def restore_collections_from_json(db, directory="scripts/backup"):
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            collection_name = filename.replace(".json", "")
            collection = db[collection_name]
            with open(os.path.join(directory, filename), "r") as json_file:
                data = json.load(json_file)
                if data:
                    collection.insert_many(data)
                    print(f"Coleção {collection_name} restaurada.")


restore_collections_from_json(db)
