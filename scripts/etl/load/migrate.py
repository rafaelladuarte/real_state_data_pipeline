from scripts.infra.storage.mongo import MongoDB
from scripts.infra.storage.postgres import PostgreDB
from scripts.infra.security.secrets import get_secret_value


def treat_data_to_postgres():
    print("---------------- RAW DATA TO POSTGRES----------------")
    mongo = MongoDB(
        uri=get_secret_value("MONGO_URI")
    )

    postgres = PostgreDB(
        uri=get_secret_value("POSTGRESQL_URI")
    )
    # postgres._create_database()

    list_collection_names = [
        "treat_imoveis",
        "treat_imobiliarias"
    ]
    for collection_name in list_collection_names:
        print(f"Get documents in collection '{collection_name}'")
        documents = mongo.get_documents(
            query={},
            collection=collection_name
        )

        table_name = "_" + collection_name

        print(f"Insert documents in table '{table_name}'")
        postgres.post_dataframe(
            collection_name=table_name,
            documents=documents
        )


if __name__ == '__main__':
    treat_data_to_postgres()
