from scripts.infra.storage.mongo import MongoDB
from scripts.infra.security.secrets import get_secret_value
from scripts.utility.operator import (
    extract_date, extract_number, extract_address
)


def treat_real_state():
    print("---------------- TREATMENT REAL STATE----------------")

    mongo = MongoDB(
        uri=get_secret_value('MONGO_URI')
    )

    mongo.create_hash_index(
        collection="treat_imobiliarias",
        hash="id_imobiliaria"
    )

    b = 0
    while True:
        b += 1

        print(f"=> Batch {b}")
        print("Get documents in collection 'raw_imobiliarias'")
        docs = mongo.get_documents(
            query={
                'treat': {
                    "$exists": False
                },
            },
            collection='raw_imobiliarias'
        )

        if len(docs) == 0:
            break

        data = []
        list_id = []
        for doc in docs:
            list_id.append(doc["_id"])
            data_cadastro = extract_date(doc["data_cadastro_imobiliaria"])[0]

            street, number, district = extract_address(
                doc["endereco_imobiliaria"]
            )

            data.append(
                {
                    "id_imobiliaria": extract_number(doc["imobiliaria"]),
                    "nome_imobiliaria": doc["nome_imobiliaria"],
                    "credencial_imobiliaria": doc["credencial_imobiliaria"],
                    "quantidade_imovel": extract_number(
                        doc["quantidade_imovel"]
                    ),
                    "endereco_completo": doc["endereco_imobiliaria"],
                    "rua": street,
                    "bairro": district,
                    "numero": number,
                    "data_cadastro": data_cadastro,
                    "telefone": None,
                    "data_coleta": doc["data_coleta_imobiliaria"]
                }
            )

        print("Update documents in collection 'raw_imoveis'")
        mongo.update_documents(
            query={
                "_id": {
                    "$in": list_id
                }
            },
            set={
                "$set": {
                    "treat": True
                }
            },
            collection='raw_imobiliarias'
        )

        print("Insert documents in collection 'treat_imobiliarias'")
        mongo.insert_documents(
            documents=data,
            collection='treat_imobiliarias'
        )


if __name__ == '__main__':
    treat_real_state()
