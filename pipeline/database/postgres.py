from sqlalchemy import create_engine

import pandas as pd

import os


class PostreSQL:
    def __init__(self):
        self.psql = create_engine(os.environ["POSTGRESQL_URI"])

    def post_data(self, collection, documents, ):
        df = pd.DataFrame(documents)
        df.to_sql(collection, self.psql, if_exists='replace', index=False)
