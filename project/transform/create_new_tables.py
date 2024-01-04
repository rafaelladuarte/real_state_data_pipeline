from project.database.postgres import PostreSQL
from pathlib import Path

import re


def create_tables_new_schema():
    psql = PostreSQL()
    psql._create_schema(schema_name="star_schema")

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
        file = Path(f"./project/sql/create_table/{table}.sql")
        sql = file.read_text()
        query = re.sub(r"[\n\t]", "", sql)
        psql.execute_query_direct(table, query)


if __name__ == "__main__":
    create_tables_new_schema()
