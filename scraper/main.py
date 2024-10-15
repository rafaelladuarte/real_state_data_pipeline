from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By

# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support import expected_conditions as EC

from time import sleep
import pandas as pd


def config_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument('--disable-gpu')
    # options.add_argument("--headless")
    options.add_experimental_option(
        "excludeSwitches",
        ["enable-automation"]
    )
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)

    stealth(
        driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True
    )
    return driver


data = []
tipos = [
    "casas",  "apartamentos", "studio",
    # "quitinetes", "casas-de-condominio",
    # "cobertura", "flat", "float"
]
for tipo in tipos:
    url = f"https://www.zapimoveis.com.br/venda/{tipo}/mg+uberlandia/"

    sleep(5)
    driver = config_driver()
    driver.get(url)
    driver.implicitly_wait(10)

    cards_container = driver.find_element(
        By.CLASS_NAME,
        "listing-wrapper__content"
    )

    cards = cards_container.find_elements(
        By.CLASS_NAME,
        "BaseCard_card__content__pL2Vc"
    )

    for card in cards:
        titulo = card.find_element(By.CSS_SELECTOR, "h2 > span").text
        endereco = card.find_element(
            By.CSS_SELECTOR, "h2 > span:nth-child(2)"
        ).text
        area = card.find_element(
            By.CSS_SELECTOR, "p[itemprop='floorSize']"
        ).text
        quartos = card.find_element(
            By.CSS_SELECTOR, "p[itemprop='numberOfRooms']"
        ).text
        banheiros = card.find_element(
            By.CSS_SELECTOR, "p[itemprop='numberOfBathroomsTotal']"
        ).text
        vagas = card.find_element(
            By.CSS_SELECTOR,
            "p[data-testid='card-amenity'][data-cy='rp-cardProperty-parkingSpacesQuantity-txt']"
        ).text
        preco = card.find_element(
            By.CSS_SELECTOR, "div[data-cy='rp-cardProperty-price-txt'] p"
        ).text
        link = card.find_element(
            By.XPATH,
            '//*[@id="__next"]/main/section/div/form/div[2]/div[4]/div[1]/div/div[3]/div/a'
        ).get_attribute("href")

        data.append({
            "titulo": titulo,
            "endereco": endereco,
            "area": area,
            "quartos": quartos,
            "banheiros": banheiros,
            "garagem": vagas,
            "preco": preco,
            "url": link,
            "tipo": tipo
        })

    driver.quit()

pd.DataFrame.from_dict(data).to_csv("scraper/main.csv")
