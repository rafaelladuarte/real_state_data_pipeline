from selenium.webdriver.common.by import By
from scraper import WebScraper

import pandas as pd

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

        if link:
            data.append({"links": link})

pd.DataFrame.from_dict(data).to_csv("scr/scraper/csv/links.csv", index=False)
