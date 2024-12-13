from scripts.infra.storage.mongo import MongoDB
from scripts.infra.security.secrets import get_secret_value
from scripts.utility.operator import (
    extract_date, extract_number, extract_address
)
from scripts.etl.treatment.images import treatment_images


def treat_property():
    print("---------------- TREATMENT PROPERTY ----------------")

    mongo = MongoDB(
        uri=get_secret_value('MONGO_URI')
    )

    b = 0
    while True:
        b += 1

        if b == 3:
            break

        print(f"=> Batch {b}")
        print("Get documents in collection 'raw_imoveis'")
        docs = mongo.get_documents(
            query={
                'treat': {
                    "$exists": False
                },
            },
            collection='raw_imoveis'
        )

        if len(docs) == 0:
            break

        data = []
        list_id = []
        for doc in docs:
            list_id.append(doc["_id"])
            data_cadastro, data_atualizacao = extract_date(doc["data_anuncio"])
            data_coleta = extract_date(doc["data_coleta_imovel"])[0]

            street, number, district = extract_address(doc["endereco"])

            images = treatment_images(doc["original_imagens"])

            data.append(
                {
                    "titulo_anuncio": doc["titulo_anuncio"],
                    "tipo_imovel": doc["tipo_imovel"],
                    "modo_imovel": doc["modo_imovel"],
                    "descricao": doc["descricao"],
                    "preco": extract_number(doc["preco"]),
                    "condominio": extract_number(doc["condominio"]),
                    "iptu": extract_number(doc["iptu"]),
                    "area": extract_number(doc["area"]),
                    "quartos": extract_number(doc["quartos"]),
                    "banheiro": extract_number(doc["banheiro"]),
                    "vagas": extract_number(doc["vagas"]),
                    "suite": extract_number(doc["suite"]),
                    "outros": doc["outros"],
                    "endereco_completo": doc["endereco"],
                    "rua": street,
                    "bairro": district,
                    "numero": number,
                    "telefone": doc["telefone"],
                    "id_imobiliaria": extract_number(doc["imobiliaria_url"]),
                    "imagens": images,
                    "data_cadastro": data_cadastro,
                    "data_atualizacao": data_atualizacao,
                    "data_coleta_imovel": data_coleta
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
                    "scraper": True
                }
            },
            collection='raw_imoveis'
        )

        print("Insert documents in collection 'treat_imoveis'")
        mongo.insert_documents(
            documents=data,
            collection='treat_imoveis'
        )


if __name__ == '__main__':
    treat_property()
