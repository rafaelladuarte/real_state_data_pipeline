from infra.security.secrets import get_secret_value

from datetime import datetime

import subprocess
import os


def backup_mongo():

    mongo_uri = get_secret_value("MONGO_URI")
    backup_dir = "backup/"

    today = datetime.now().strftime("%Y%m%d")
    backup_path = os.path.join(backup_dir, f"backup_{today}")

    if not os.path.exists(backup_path):
        os.makedirs(backup_path)

    command = [
        "mongodump",
        "--uri", mongo_uri,
        "--out", backup_path
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Backup concluído com sucesso em {backup_path}")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o backup: {e}")


backup_mongo()
