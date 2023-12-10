from project.database.postgres import PostreSQL


def config_schema():
    psql = PostreSQL()
    psql._create_schema(schema_name="star_schema")
    psql._create_extesion_uuid()


if __name__ == "__main__":
    config_schema()
