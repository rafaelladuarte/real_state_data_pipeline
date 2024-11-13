from selenium.webdriver.common.by import By
from scraper import WebScraper

from utility.operator import (
    extract_date, extract_number
)
from storage.mongo import MongoDB
from security.secrets import get_secret_value

from time import sleep

import re

mongo = MongoDB(
    uri=get_secret_value('MONGO_URI')
)
scraper = WebScraper()

docs = mongo.get_documents(
    flag='get_mobi',
    database='scraper',
    collection='imoveis'
)

data = []
list_id = []
for doc in docs[:10]:

    mobi_id = doc['imobiliaria_id']
    list_id.append(doc['id'])

    link = "https://www.zapimoveis.com.br/imobiliaria/" + mobi_id

    scraper = WebScraper()
    scraper.get_driver(link)

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
        path="p[data-testid='publisher-creci']",
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
           "id": mobi_id,
           "nome": name,
           "credencial": credential,
           "quantidade_imovel": extract_number(imovel_qt),
           "data_cadastro": extract_date(created_dt)[0],
           "telefone": None   # ERRO
        }
     )

    scraper.close_driver()

    sleep(2)

mongo.update_documents(
    ids=list_id,
    flag="get_mobi",
    database='scraper',
    collection='imoveis'
)

mongo.insert_documents(
    documents=data,
    database='scraper',
    collection='imobiliarias'
)
