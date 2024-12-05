from scripts.infra.security.secrets import get_secret_value

import subprocess


def restore_mongo():

    mongo_uri = get_secret_value("MONGO_URI")
    backup_dir = "/caminho/do/backup/backup_YYYYMMDD"

    command = [
        "mongorestore",
        "--uri", mongo_uri,
        "--drop",
        backup_dir
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Restauração concluída com sucesso do diretório {backup_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao restaurar o backup: {e}")


restore_mongo()
