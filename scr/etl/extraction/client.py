from infra.storage.mongo import MongoDB
from infra.security.secrets import get_secret_value
from utility.generator import (
    generator_email, generator_name, generator_phone
)

from datetime import datetime

import random


def generator_client():
    print("---------------- CLIENT ----------------")

    mongo = MongoDB(
        uri=get_secret_value('MONGO_URI')
    )

    print("Get documents in collection 'corretor'")
    docs = mongo.get_documents(
        query={},
        collection="corretor"
    )

    print("Colect 'id_corretor'")
    realtor_ids = [doc["_id"] for doc in docs]

    print("Generator clients")
    data_client = []
    for i in range(0, 20):
        name = generator_name()
        email = generator_email(name)
        phone = generator_phone()

        data_client.append(
            {
                "id_cliente": i,
                "nome_cliente": name,
                "telefone_cliente": phone,
                "email_cliente": email,
                "data_cadastro_cliente": datetime.now().strftime(
                    "%d-%m-%Y %H:%M:%S"
                ),
                "id_corretor": str(random.choice(realtor_ids)),
            }
        )

    print("Insert documents in collection 'cliente'")
    mongo.insert_documents(
        documents=data_client,
        collection="client"
    )


if __name__ == '__main__':
    generator_client()
