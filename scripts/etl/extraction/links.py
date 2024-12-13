from selenium.webdriver.common.by import By

from scripts.etl.extraction.scraper import WebScraper
from scripts.infra.storage.mongo import MongoDB
from scripts.infra.security.secrets import get_secret_value

from datetime import datetime
from time import sleep

mongo = MongoDB(
    uri=get_secret_value('MONGO_URI')
)


def get_links_property():
    tipos = [
        # "casas",
        # "apartamentos",
        "studio",
        # "quitinetes", "casas-de-condominio",
        # "cobertura", "flat", "float",
    ]
    for tipo in tipos:
        print(f"---------------- {tipo.upper()} ----------------")
        url = f"https://www.zapimoveis.com.br/venda/{tipo}/mg+uberlandia/"

        data = []

        scraper = WebScraper()
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

        print("Get information")
        for full_card in list_cards:
            n = full_card.get_attribute("data-position")
            card = scraper.get_element(
                by=By.CLASS_NAME,
                path="BaseCard_card__content__pL2Vc",
                driver_element=full_card
            )

            link = scraper.get_element(
                by=By.XPATH,
                path=f'//*[@id="__next"]//div[{n}]/div/a',
                attribute_type="href",
                driver_element=card
            )

            allowed_prefix = 'https://www.zapimoveis.com.br/imovel/'

            if link and link.startswith(allowed_prefix):
                data.append(
                    {
                        "link": link,
                        "tipo": tipo,
                        "modo": "venda",
                        "created_dt": datetime.now().strftime(
                            "%d-%m-%Y %H:%M:%S"
                        )
                    }
                )

        scraper.close_driver()

        print("Insert documents in collection 'links_imoveis'")
        mongo.insert_documents(
            documents=data,
            collection='links_imoveis'
        )

        sleep(2)


if __name__ == '__main__':
    get_links_property()
