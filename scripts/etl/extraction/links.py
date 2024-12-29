from selenium.webdriver.common.by import By

from scripts.etl.extraction.scraper import WebScraper
from scripts.infra.storage.mongo import MongoDB

from scripts.infra.security.secrets import get_secret_value
from scripts.utility.operator import extract_number

from datetime import datetime
from time import sleep

mongo = MongoDB(
    uri=get_secret_value('MONGO_URI')
)


def get_links_property():
    tipos = [
        # "casas",
        "apartamentos",
        # "studio",
        # "quitinetes",
        # "casas-de-condominio",
        # "cobertura", "flat", "float",
    ]
    modos = ["venda", "aluguel"]

    blends = [
        (
            modo,
            tipo
        )
        for tipo in tipos
        for modo in modos
    ]

    for modo, tipo in blends:

        url = f"https://www.zapimoveis.com.br/{modo}/{tipo}/mg+uberlandia/"

        print(f"----------- {tipo.upper()} {modo.upper()} -----------")

        scraper = WebScraper()
        scraper.get_driver(url)

        sleep(2)

        property_result = scraper.get_element(
            by=By.CLASS_NAME,
            path='result-wrapper__title',
        )

        property_qtf = scraper.get_element(
            by=By.TAG_NAME,
            path='h1',
            attribute_type='text',
            driver_element=property_result
        )

        qtf = extract_number(property_qtf)
        pages = int((qtf/50) - 1)

        scraper.close_driver()

        for page in range(1, pages):
            data = []

            if page == 4:
                break

            print(f"- PÁGINA {page}")

            scraper = WebScraper()
            scraper.get_driver(url + f"?pagina={page}")

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
                            "modo": modo,
                            "created_dt": datetime.now().strftime(
                                "%d-%m-%Y %H:%M:%S"
                            )
                        }
                    )

            print("Insert documents in collection 'links_imoveis'")
            mongo.insert_documents(
                documents=data,
                collection='links_imoveis'
            )

            sleep(2)

            scraper.close_driver()

            sleep(2)


if __name__ == '__main__':
    get_links_property()
