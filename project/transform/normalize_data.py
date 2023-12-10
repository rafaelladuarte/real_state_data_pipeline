from project.database.postgres import PostreSQL


def normalize_data():
    psql = PostreSQL()
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
        psql.execute_query()


if __name__ == "__main__":
    normalize_data()
