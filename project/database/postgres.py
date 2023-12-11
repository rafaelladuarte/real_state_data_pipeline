from sqlalchemy_utils import create_database
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.schema import CreateSchema
from sqlalchemy import text

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

    def _create_schema(self, schema_name: str) -> None:
        """
        Cria um esquema de dados no banco de dados olist

        Args:
            schema_name (str): nome do schema que será criado
        """

        engine = create_engine(self._uri + "/olist")

        with engine.connect() as connection:
            connection.execute(CreateSchema(schema_name, if_not_exists=True))
            connection.commit()

    def _create_extesion_uuid(self) -> None:
        """
        Cria a extensão que permite o uso do tipo de dado UUID
        """

        engine = create_engine(self._uri + "/olist")

        with engine.connect() as connection:
            connection.execute(text('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"'))
            connection.commit()

    def post_dataframe(
        self, schema_name: str, collection_name: str, documents: list[dict]
    ) -> None:
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
            if_exists="replace",
            index=False,
            schema=schema_name,
        )

        engine.dispose()

    def execute_query_direct(
        self,
        table: str,
        query: str,
    ):
        """
        Executa uma query direta no SQL no banco de dados olist.

        Arg:
            table (str): nome da tabela a ser consultada.
            query (str): consulta a ser executada
        """
        try:
            engine = create_engine(self._uri + "/olist")
            with engine.connect() as connection:
                connection.execute(text(query))
                connection.commit()
            print(f"Sucesso ao executar consultas SQL da tabela {table}")
        except Exception as e:
            print(f"Erro ao executar consultas SQL da tabela {table}: {e}")

        return None

    def execute_query_transaction(
        self,
        table: str,
        query: str,
    ):
        """
        Executa uma query que envolvem transações e manipulação de objetos
        no SQL no banco de dados olist.

        Arg:
            table (str): nome da tabela a ser consultada.
            query (str): consulta a ser executada
        """
        try:
            engine = create_engine(self._uri + "/olist")
            with Session(engine) as session:
                session.execute(text(query))
                session.commit()
            print(f"Sucesso ao executar consultas SQL da tabela {table}")
        except Exception as e:
            print(f"Erro ao executar consultas SQL da tabela {table}: {e}")

        return None
