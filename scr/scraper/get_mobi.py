from selenium.webdriver.common.by import By
from scraper import WebScraper

from utility.operator import (
    extract_date, extract_number
)
from time import sleep

import pandas as pd
import csv
import re

scraper = WebScraper()

mobi_ids = []
with open("scr/scraper/csv/info_imoveis.csv", encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    next(reader, None)
    for row in reader:
        mobi_ids.append(row['mobi_id'])

mobi_ids = list(set(mobi_ids))

data = []
for mobi_id in mobi_ids:
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

    whatsapp_button = scraper.get_element(
        by=By.XPATH,
        path="//button[@data-testid='l-button' and @aria-label='WhatsApp']",
        attribute_type="button"
    )   # Botão para coletar o link do whatsaap

    sleep(3)

    page_whats = scraper.change_last_page()

    whatsapp_link = scraper.get_element(
        by=By.XPATH,
        path="//a[contains(@href, 'https://wa.me')]",
        attribute_type="href",
        driver_element=page_whats
    )

    data.append(
        {
           "id": mobi_id,
           "nome": name,
           "credencial": credential,
           "quantidade_imovel": extract_number(imovel_qt),
           "data_cadastro": extract_date(created_dt)[0],
           "telefone": extract_number(whatsapp_link)    # ERRO
        }
     )

    scraper.close_driver()

    sleep(2)

pd.DataFrame.from_dict(data).to_csv(
    "scr/scraper/csv/info_imobiliarias.csv",
    index=False
)
