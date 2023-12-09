from project.database.postgres import PostreSQL
from project.database.mongo import MongoDB


def data_to_postgresql():
    psql = PostreSQL()
    psql._create_database()
    psql._create_schema("olist_raw")
    collections = MongoDB().list_collections()
    for collection in collections:
        documentos = MongoDB().get_data(collection=collection)
        psql.post_dataframe(
            schema_name="olist_raw", collection_name=collection, documents=documentos
        )


if __name__ == "__main__":
    data_to_postgresql()
