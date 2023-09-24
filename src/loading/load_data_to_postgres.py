from database.mongo import Mongo
from database.postgres import PostreSQL


def data_to_postgresql():
    collections = Mongo().list_collections()
    for collection in collections:
        documentos = Mongo().get_data(collection=collection)
        PostreSQL().post_data(collection=collection, documents=documentos)


if __name__ == "__main__":
    data_to_postgresql()
