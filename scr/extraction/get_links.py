from selenium.webdriver.common.by import By

from scraper import WebScraper
from storage.mongo import MongoDB
from security.secrets import get_secret_value

from datetime import datetime
# import pandas as pd

mongo = MongoDB(
    uri=get_secret_value('MONGO_URI')
)
scraper = WebScraper()

data = []
tipos = [
    "casas",
    "apartamentos",
    # "studio",
    # "quitinetes", "casas-de-condominio",
    # "cobertura", "flat", "float"
]
for tipo in tipos:
    print(f"Get {tipo}")
    url = f"https://www.zapimoveis.com.br/venda/{tipo}/mg+uberlandia/"

    scraper.get_driver(url)

    print("Scroll down page...")
    scraper.scroll_until_element_stops_moving(
        "aside.campaign[data-cy='campaign']"
    )

    print("Get cards in container")
    cards_container = scraper.get_element(
        by=By.CLASS_NAME,
        path="listing-wrapper__content",
    )
    list_cards = scraper.get_elements(
        by=By.CSS_SELECTOR,
        path='div[data-position]',
        driver_element=cards_container,
    )

    print("Get infos")
    for full_card in list_cards:
        n = full_card.get_attribute("data-position")
        card = scraper.get_element(
            by=By.CLASS_NAME,
            path="BaseCard_card__content__pL2Vc",
            driver_element=full_card
        )
        # ALGUNS PEGA OUTROS NÃO ,TENTA CRIAR O LINK AO INVES DE PEGA PRONTO
        link = scraper.get_element(
            by=By.XPATH,
            # path=f'//*[@id="__next"]/main/section/div/
            # form/div[2]/div[4]/div[1]/div/div[{n}]/div/a',
            path=f'//*[@id="__next"]//div[{n}]/div/a',
            attribute_type="href",
            driver_element=card
        )

        allowed_prefix = 'https://www.zapimoveis.com.br/imovel/'

        if link and link.startswith(allowed_prefix):
            data.append(
                {
                    "link": link,
                    "created_dt": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                }
            )

mongo.insert_documents(
    documents=data,
    database='scraper',
    collection='links_imoveis'
)
