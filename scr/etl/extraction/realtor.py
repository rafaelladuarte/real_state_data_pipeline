from infra.storage.mongo import MongoDB
from infra.security.secrets import get_secret_value
from utility.generator import (
    generator_email, generator_name, generator_phone, generator_creci
)

from datetime import datetime

import random


def generator_realtor():
    print("---------------- REALTOR ----------------")

    mongo = MongoDB(
        uri=get_secret_value('MONGO_URI')
    )

    print("Get documents in collection 'imobiliarias'")
    docs = mongo.get_documents(
        query={},
        collection="imobiliarias"
    )

    print("Colect 'id_imobiliarias'")
    mobi_ids = [doc["id_imobiliaria"] for doc in docs]

    print("Generator realtors")
    data_realtor = []

    for i in range(0, 10):
        name = generator_name()
        email = generator_email(name)
        phone = generator_phone()
        creci = generator_creci()

        data_realtor.append(
            {
                "id_corretor": i,
                "nome_corretor": name,
                "credencial_corretor": creci,
                "telefone_corretor": phone,
                "email_corretor": email,
                "id_imobiliaria": random.choice(mobi_ids),
                "data_cadastro_corretor": datetime.now().strftime(
                    "%d-%m-%Y %H:%M:%S"
                )
            }
        )

    print("Insert documents in collection 'corretor'")
    mongo.insert_documents(
        documents=data_realtor,
        collection="corretor"
    )


if __name__ == '__main__':
    generator_realtor()
