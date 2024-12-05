from sqlalchemy_utils import create_database
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.schema import CreateSchema
from sqlalchemy import text

import pandas as pd


class PostgreDB:
    def __init__(self, uri):
        self._uri = uri

    def _create_database(self) -> None:
        engine = create_engine(self._uri)
        create_database(engine.url)
        engine.dispose()

    def _create_schema(self, schema_name: str) -> None:
        engine = create_engine(self._uri)

        with engine.connect() as connection:
            connection.execute(CreateSchema(schema_name, if_not_exists=True))
            connection.commit()

    def _create_extesion_uuid(self) -> None:
        engine = create_engine(self._uri)

        with engine.connect() as connection:
            connection.execute(
                text('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"')
            )
            connection.commit()

    def post_dataframe(
        self,
        collection_name: str,
        documents: list[dict],
    ) -> None:
        engine = create_engine(self._uri)

        documents = [
            {k: v for k, v in document.items() if k != "_id"}
            for document in documents
        ]

        df = pd.DataFrame(documents)
        df.to_sql(
            name=collection_name,
            con=engine,
            if_exists="replace",
            index=False,
        )

        engine.dispose()

    def execute_query_direct(
        self,
        table: str,
        query: str,
    ):
        try:
            engine = create_engine(self._uri)
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
        try:
            engine = create_engine(self._uri)
            with Session(engine) as session:
                session.execute(text(query))
                session.commit()
            print(f"Sucesso ao executar consultas SQL da tabela {table}")
        except Exception as e:
            print(f"Erro ao executar consultas SQL da tabela {table}: {e}")

        return None

    def execute_file_sql(
        self,
        file: str,
    ):
        try:
            engine = create_engine(self._uri)
            with Session(engine) as session:
                session.execute(text(file))
                session.commit()
        except Exception as e:
            print(e)

        return None
