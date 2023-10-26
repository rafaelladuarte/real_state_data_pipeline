from sqlalchemy_utils import create_database
from sqlalchemy import create_engine

import pandas as pd

import os


class PostreSQL:
    def __init__(self):
        self._uri = os.environ["POSTGRESQL_URI"]

    def _create_database(self) -> None:
        """
        Cria um banco de dados no PostgreSQL.
        """
        engine = create_engine(self._uri + "/olist")
        create_database(engine.url)
        engine.dispose()

    def post_data(self, collection_name: str, documents: list[dict]) -> None:
        """
        Publica dados em uma coleção do banco de dados PostgreSQL.

        Args:
            collection_name (str): nome da coleção onde os dados serão
            postados.
            documents (list[dict]): dicionário de documentos a serem postados
            na coleção.
        """
        engine = create_engine(self._uri + "/olist")
        df = pd.DataFrame(documents)
        df.drop(columns=["_id"], inplace=True)
        df.to_sql(
            name=collection_name,
            con=engine,
            if_exists='replace',
            index=False
        )
        engine.dispose()