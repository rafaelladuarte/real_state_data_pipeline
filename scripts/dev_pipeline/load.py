from scripts.etl.load.migrate import treat_data_to_postgres
from scripts.infra.security.secrets import get_secret_value
from scripts.infra.storage.postgres import PostgreDB

postgres = PostgreDB(
    uri=get_secret_value("POSTGRESQL_URI")
)

treat_data_to_postgres()

files_sql = [
    'scr/etl/modeling/create_tables_oficial.sql',
    'scr/etl/modeling/insert_tables_oficial.sql',
]

print('----------- EXECUTE QUERY ----------')
for file in files_sql:
    print(f'- {file}')
    with open(file, 'r') as file:
        sql = file.read()

    cmds_sql = [cmd.strip() for cmd in sql.split(';') if cmd.strip()]

    for cmd in cmds_sql:
        if cmd .startswith('--'):
            continue
        postgres.execute_file_sql(cmd)
