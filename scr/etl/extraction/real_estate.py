from selenium.webdriver.common.by import By
from etl.extraction.scraper import WebScraper

from utility.operator import (
    extract_date, extract_number
)
from infra.storage.mongo import MongoDB
from infra.security.secrets import get_secret_value

from datetime import datetime
from time import sleep

import re


def get_real_state():
    print("---------------- REAL STATE ----------------")

    mongo = MongoDB(
        uri=get_secret_value('MONGO_URI')
    )
    scraper = WebScraper()

    pipeline = [
        {
            "$match": {
                "get_mobi": {"$exists": False}
            }
        },
        {
            "$group": {
                "_id": "$id_imobiliaria",
                "document_ids": {
                    "$push": "$_id"
                }
            }
        }
    ]

    print("Get documents in collection 'imoveis'")
    docs = mongo.get_documents_aggregate(
        pipeline=pipeline,
        collection='imoveis'
    )

    print("Get 'id_imobiliaria'")
    list_id_imoveis = []
    list_all_mobi_id = []
    for doc in docs[:100]:
        list_id_imoveis.extend(doc['document_ids'])
        list_all_mobi_id.append(doc["_id"])

    print("Filter news 'id_imobiliaria'")
    list_find_mobi_id = mongo.find_missing_mobi_ids(
        mobi_ids=list_all_mobi_id
    )

    print('Start Scraper Real State')
    data = []
    list_get_mobi_id = []
    for mobi_id in list_find_mobi_id[:10]:
        link = "https://www.zapimoveis.com.br/imobiliaria/" + str(mobi_id)

        scraper = WebScraper()
        scraper.get_driver(link)

        try:
            name = scraper.get_element(
                by=By.CLASS_NAME,
                path='publisher-heading__container',
                attribute_type="text"
            )

            credential = scraper.get_element(
                by=By.CSS_SELECTOR,
                path="p[data-testid='publisher-creci']",
                attribute_type="text"
            )

            if credential:
                match = re.search(r"Creci:\s*(\S+)", credential)
                if match:
                    credential = match.group(1)

            address = scraper.get_element(
                by=By.CSS_SELECTOR,
                path="p[data-testid='publisher-address']",
                attribute_type="text"
            )

            infos = scraper.get_elements(
                by=By.CLASS_NAME,
                path="advertiser-info-rp__container",
            )

            imovel_qt = scraper.get_element(
                by=By.XPATH,
                path='//div[2]/p[2]',
                attribute_type="text",
                driver_element=infos[0]
            )
            created_dt = scraper.get_element(
                by=By.XPATH,
                path='//div[2]/p[3]',
                attribute_type="text",
                driver_element=infos[0]
            )

            data.append(
                {
                    "id_imobiliaria": mobi_id,
                    "nome_imobiliaria": name,
                    "credencial_imobiliaria": credential,
                    "endereco_imobiliaria": address,
                    "quantidade_imovel": extract_number(imovel_qt),
                    "data_cadastro_imobiliaria": extract_date(created_dt)[0],
                    "telefone_imobiliaria": None,   # ERRO
                    "data_coleta_imobiliaria": datetime.now().strftime(
                        "%d-%m-%Y %H:%M:%S"
                    )
                }
            )

            list_get_mobi_id.append(mobi_id)

            print(f'- {name}: {mobi_id}')

        except Exception as e:
            print(e)

        scraper.close_driver()

        sleep(2)

    if len(list_get_mobi_id) > 0:
        print("Update documents in collection 'imoveis'")
        mongo.update_documents(
            query={
                "id_imobiliaria": {
                    "$in": list_get_mobi_id
                }
            },
            set={
                "$set": {
                    "get_mobi": True,
                    "updated_dt": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                }
            },
            collection="imoveis"

        )

        print("Insert documents in collection 'imobiliarias'")
        mongo.insert_documents(
            documents=data,
            collection='imobiliarias'
        )


if __name__ == '__main__':
    get_real_state()
