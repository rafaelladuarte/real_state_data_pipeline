from project.database.postgres import PostreSQL
from project.database.mongo import MongoDB


def data_to_postgresql():
    psql = PostreSQL()
    psql._create_database()
    collections = MongoDB().list_collections()
    for collection in collections:
        documentos = MongoDB().get_data(collection=collection)
        psql.post_data(
            collection_name=collection,
            documents=documentos
        )


if __name__ == "__main__":
    data_to_postgresql()
