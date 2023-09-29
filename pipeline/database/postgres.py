from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import pandas as pd

import os


class PostreSQL:
    def __init__(self):
        self._uri = os.environ["POSTGRESQL_URI"]
        self.engine = create_engine(self._uri + "/olist")

    # def create_database(self):
    #     self.engine = create_engine(self._uri + "/olist")
    #     try:
    #         self.engine.connect()
    #     except:
    #         for table in reversed(Base.metadata.sorted_tables):
    #             engine.execute(table.delete())

    def post_data(self, collection, documents, ):
        df = pd.DataFrame(documents)
        df.to_sql(collection, self.engine, if_exists='replace', index=False)
