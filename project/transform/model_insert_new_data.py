from project.database.postgres import PostreSQL
from pathlib import Path

import re


def insert_data_to_new_tables():
    psql = PostreSQL()
    psql._create_extesion_uuid()

    list_table = [
        "geolocation",
        "sellers",
        "customers",
        "category",
        "products",
        "items",
        "payments",
        "reviews",
        "orders",
    ]

    for table in list_table:
        file = Path(f"./project/sql/insert_table/{table}.sql")
        sql = file.read_text()
        query = re.sub(r"[\n\t]", " ", sql)
        psql.execute_query_transaction(table, query)


if __name__ == "__main__":
    insert_data_to_new_tables()
