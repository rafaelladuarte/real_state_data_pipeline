from selenium.webdriver.common.by import By

from scripts.etl.extraction.scraper import WebScraper
from scripts.infra.storage.mongo import MongoDB

from scripts.infra.security.secrets import get_secret_value

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
                "_id": "$imobiliaria_url",
                "list_id": {
                    "$push": "$_id"
                }
            }
        }
    ]

    print("Get documents in collection 'imoveis'")
    docs = mongo.get_documents_aggregate(
        pipeline=pipeline,
        collection='raw_imoveis'
    )

    print("Get 'imobiliaria_url'")
    list_id_imoveis = []
    list_all_mobi_url = []
    for doc in docs[:100]:
        list_id_imoveis.extend(doc['list_id'])
        list_all_mobi_url.append(doc["_id"])

    print("Filter news 'imobiliaria_url'")
    list_find_mobi_url = mongo.find_missing_mobi_url(
        list_url=list_all_mobi_url
    )

    print('Start Scraper Real State')
    data = []
    list_get_mobi_url = []
    for mobi_url in list_find_mobi_url[:10]:
        scraper = WebScraper()
        scraper.get_driver(mobi_url)

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
                path='//section/div[2]/p[2]',
                attribute_type="text",
                # driver_element=infos[0]
            )
            created_dt = scraper.get_element(
                by=By.XPATH,
                path='//div[2]/p[3]',
                attribute_type="text",
                driver_element=infos[0]
            )

            data.append(
                {
                    "imobiliaria": mobi_url,
                    "nome_imobiliaria": name,
                    "credencial_imobiliaria": credential,
                    "endereco_imobiliaria": address,
                    "quantidade_imovel": imovel_qt,
                    "data_cadastro_imobiliaria": created_dt,
                    "telefone_imobiliaria": None,   # ERRO
                    "data_coleta_imobiliaria": datetime.now().strftime(
                        "%d-%m-%Y %H:%M:%S"
                    )
                }
            )

            list_get_mobi_url.append(mobi_url)

            print(f'- {name}')

        except Exception as e:
            print(e)

        scraper.close_driver()

        sleep(2)

    if len(list_get_mobi_url) > 0:
        print("Update documents in collection 'raw_imoveis'")
        mongo.update_documents(
            query={
                "imobiliaria": {
                    "$in": list_get_mobi_url
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

        print("Insert documents in collection 'raw_imobiliarias'")
        mongo.insert_documents(
            documents=data,
            collection='raw_imobiliarias'
        )


if __name__ == '__main__':
    get_real_state()
