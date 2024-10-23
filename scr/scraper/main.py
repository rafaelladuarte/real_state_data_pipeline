from time import sleep
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

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


def scroll_until_element_stops_moving(
        driver,
        css_selector,
        timeout=5,
        max_attempts=10
):
    previous_location = None
    attempts = 0

    element = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
    )

    while attempts < max_attempts:
        location = element.location_once_scrolled_into_view

        if previous_location is not None and location == previous_location:
            print("O elemento parou de se mover.")
            break

        driver.execute_script("arguments[0].scrollIntoView();", element)
        sleep(timeout)

        previous_location = location
        attempts += 1
        print(f"Tentativa {attempts}: elemento movido para {location}")

    return driver


def get_elements(
    driver: webdriver,
    by: By,
    path: str,
    timeout=10
):
    try:
        elements = WebDriverWait(driver, timeout).until(
            EC.presence_of_all_elements_located((by, path))
        )
    except TimeoutException:
        return None

    return elements


def get_element(
        driver: webdriver,
        by: By,
        path: str,
        type: str = None,
        timeout=10
):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, path))
        )
        if type == "text":
            element = element.text
        elif type == "href":
            element = element.get_attribute("href")

    except TimeoutException:
        return None

    return element


print("-"*40)
print('Start Scraper')

data = []
tipos = [
    "casas",
    # "apartamentos", "studio",
    # "quitinetes", "casas-de-condominio",
    # "cobertura", "flat", "float"
]
for tipo in tipos:
    print(f"Get {tipo}")
    url = f"https://www.zapimoveis.com.br/venda/{tipo}/mg+uberlandia/"

    sleep(5)
    driver = config_driver()
    driver.get(url)

    print("Scroll down page...")
    driver = scroll_until_element_stops_moving(
        driver,
        "aside.campaign[data-cy='campaign']"
    )

    print("Get cards in container")
    cards_container = get_element(
        driver, By.CLASS_NAME, "listing-wrapper__content"
    )
    list_cards = get_elements(
        cards_container,
        By.CSS_SELECTOR,
        'div[data-position]'
    )

    print("Get infos")
    for full_card in list_cards:
        n = full_card.get_attribute("data-position")
        card = get_element(
            full_card,
            By.CLASS_NAME,
            "BaseCard_card__content__pL2Vc"
        )
        titulo = get_element(
            card,
            By.CSS_SELECTOR,
            "h2 > span",
            "text"
        )
        endereco = get_element(
            card,
            By.CSS_SELECTOR,
            "h2 > span:nth-child(2)",
            "text"
        )
        area = get_element(
            card,
            By.CSS_SELECTOR,
            "p[itemprop='floorSize']",
            "text"
        )
        quartos = get_element(
            card,
            By.CSS_SELECTOR,
            "p[itemprop='numberOfRooms']",
            "text"
        )
        banheiros = get_element(
            card,
            By.CSS_SELECTOR,
            "p[itemprop='numberOfBathroomsTotal']",
            "text"
        )
        vagas = get_element(
            card,
            By.CSS_SELECTOR,
            "p[data-testid='card-amenity']",
            #   '[data-cy='rp-cardProperty-parkingSpacesQuantity-txt']",
            "text"
        )
        preco = get_element(
            card,
            By.CSS_SELECTOR,
            "div[data-cy='rp-cardProperty-price-txt'] p",
            "text"
        )
        # ALGUNS PEGA OUTROS NÃO ,TENTA CRIAR O LINK AO INVES DE PEGA PRONTO
        link = get_element(
            card,
            By.XPATH,
            '//*[@id="__next"]/main/section/div/form/div[2]/div[4]/9',
            #   div[1]/div/div[{n}]/div/a',
            "href"
        )

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

pd.DataFrame.from_dict(data).to_csv("scraper/main2.csv")
