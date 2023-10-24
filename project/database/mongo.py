from pymongo import MongoClient
import os


class MongoDB:
    def __init__(self):
        cli = MongoClient(host=os.environ["MONGO_URI"])
        self.db = cli["olist_raw"]

    def list_collections(self) -> list:
        """
        Lista as coleções disponíveis no banco de dados MongoDB.

        Returns:
            list: Uma lista de nomes de coleções disponíveis no banco de dados.
        """
        return self.db.list_collection_names()

    def get_data(self, collection: str) -> list[dict]:
        """
        Obtém dados de uma coleção específica do banco de dados.

        Args:
            collection (str): nome da coleção a partir da qual os dados serão
            obtidos.

        Returns:
            list[dict]: lista de documentos (dicionários) obtidos da coleção.
        """
        cursor = self.db[collection].find()
        documents = []

        for c in cursor:
            documents.append(c)

        return documents

    def post_data(self, collection: str, data: list[dict]) -> None:
        """
        Publica dados em uma coleção específica do banco de dados MongoDB.

        Args:
            collection (str): O nome da coleção onde os dados serão postados.
            data (list[dict]): Uma lista de documentos (dicionários) a serem
            postados na coleção.

        Raises:
            pymongo.errors.BulkWriteError: Se ocorrer um erro ao postar os
            dados na coleção.
        """
        col = self.db[collection]
        col.insert_many(data)
