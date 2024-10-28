from selenium.webdriver.common.by import By
from scraper import WebScraper
from utility.generator import (
    generator_email, generator_name, generator_phone
)
from utility.operator import (
    extract_date, extract_number
)
from time import sleep

import pandas as pd
import csv


links = []
with open("scr/scraper/links.csv", encoding='utf-8') as csvf:
    reader = csv.reader(csvf)
    next(reader, None)
    for row in reader:
        links.append(row[0])

forbidden_exact = 'https://www.zapimoveis.com.br/'
forbidden_prefix = 'https://www.zapimoveis.com.br/imobiliaria/'
filtered_links = [
    link for link in links
    if link != forbidden_exact and not link.startswith(forbidden_prefix)
]


data = []
for link in filtered_links[1:10]:
    scraper = WebScraper()
    scraper.get_driver(link)

    # COLETA LINK DAS IMAGENS
    carousel_images = scraper.get_elements(
        by=By.CSS_SELECTOR,
        path='ul.carousel-photos--wrapper'
    )

    image_urls = []
    for li in carousel_images:
        srcset = scraper.get_element(
            by=By.CLASS_NAME,
            path="carousel-photos--img",
            attribute_type="srcset",
            driver_element=li
        )
        if srcset:
            largest_image_url = srcset.split(",")[-1].strip().split(" ")[0]
            image_urls.append(largest_image_url)

    # COLETA DAS INFORMAÇÕES BASICAS
    details = scraper.get_element(
        by=By.CLASS_NAME,
        path='details'
    )

    address = scraper.get_element(
        by=By.CSS_SELECTOR,
        path="p[data-testid='address-info-value']",
        attribute_type="text",
        driver_element=details,
    )
    price = scraper.get_element(
        by=By.CSS_SELECTOR,
        path="p[data-testid='price-info-value']",
        attribute_type="text",
        driver_element=details,
    )
    cond = scraper.get_element(
        by=By.ID,
        path="condo-fee-price",
        attribute_type="text",
        driver_element=details,
    )
    iptu = scraper.get_element(
        by=By.ID,
        path="iptu-price",
        attribute_type="text",
        driver_element=details,
    )

    # COLETA DA LISTA DE COMODIDATES
    amenities_list = scraper.get_element(
        by=By.CLASS_NAME,
        path="amenities-list",
        driver_element=details
    )
    span_elements = scraper.get_elements(
        by=By.TAG_NAME,
        path="span",
        driver_element=amenities_list
    )
    amenities = [span.text for span in span_elements if span.text.strip()]

    area, bedroom, bathroom = None, None, None
    garage, suites = None, None
    others = []

    for amenitie in amenities:
        if "m²" in amenitie:
            area = extract_number(amenitie)
        elif "quarto" in amenitie:
            bedroom = extract_number(amenitie)
        elif "banheiro" in amenitie:
            bathroom = extract_number(amenitie)
        elif "vaga" in amenitie:
            garage = extract_number(amenitie)
        elif "suíte" in amenitie:
            suites = extract_number(amenitie)
        else:
            others.append(amenitie)

    # COLETA DE OUTROS DADOS DO ANUNCIO
    container = scraper.get_element(
        by=By.CLASS_NAME,
        path="desktop-only-container"
    )

    title = scraper.get_element(
        by=By.XPATH,
        path='//div[@class="stack small column"]//h1',
        attribute_type="text",
        driver_element=container
    )
    scraper.get_element(
        by=By.CLASS_NAME,
        path='collapse-toggle-button',
        attribute_type="button",
        driver_element=container
    )   # Botão para visualizar a descrição completa

    p = "p[@data-testid='description-content']"
    describe = scraper.get_element(
        by=By.XPATH,
        path=f"//div[contains(@class, 'collapse-content')]//{p}",
        attribute_type="text",
        driver_element=container
    )

    # COLETA DAS INFORMAÇÕES DA IMOBILIARIA OU RESPONSAVEL
    url_mobi = scraper.get_element(
        by=By.XPATH,
        path="//a[@data-testid='official-store-redirect-link']",
        attribute_type="href",
    )
    mobi = scraper.get_element(
        by=By.XPATH,
        path="//a[@data-testid='official-store-redirect-link']",
        attribute_type="text",
    )

    # COLETA DA DATA DE CRIAÇÃO DO ANUNCIO
    create_update = scraper.get_element(
        by=By.CSS_SELECTOR,
        path="div[data-testid='info-date']",
        attribute_type="text"
    )
    if create_update:
        create_dt, update_dt = extract_date(create_update)

    # PREENCHENDO FORMULARIO DE COLETA DE TELEFONE
    name_gerado = generator_name()
    phone_gerado = generator_phone()
    email_gerado = generator_email(name_gerado)

    scraper.get_element(
        by=By.XPATH,
        path="//button[@data-cy='ldp-viewPhone-btn']",
        attribute_type="button"
    )

    name = scraper.get_element(
        by=By.XPATH,
        path="//input[@data-cy='lead-modalPhone-name-inp']"
    )
    name.send_keys(name_gerado)

    email = scraper.get_element(
        by=By.XPATH,
        path="//input[@data-cy='lead-modalPhone-email-inp']"
    )
    email.send_keys(email_gerado)

    phone = scraper.get_element(
        by=By.XPATH,
        path="//input[@data-cy='lead-modalPhone-phone-inp']"
    )
    phone.send_keys(phone_gerado)

    scraper.get_element(
        by=By.ID,
        path="adopt-accept-all-button",
        attribute_type="button"
    )   # Botão para fechar modal de cookies

    scraper.get_element(
        by=By.XPATH,
        path="//button[@data-cy='lead-modalPhone-sendData-btn']",
        attribute_type="button"
    )

    sleep(5)

    fail_phone = scraper.get_element(
        by=By.CLASS_NAME,
        path='FailedFeedback_failed-contact__content__lL4Gz'
    )

    # COLETA DA LISTA DE TELEFONES
    contacts = []
    if fail_phone is None:
        list_phone = scraper.get_elements(
            by=By.XPATH,
            path="//a[@data-cy='lead-modalPhone-phonesList-txt']",
        )

        for phone in list_phone:
            tel = phone.get_attribute("href").replace("tel:", "")
            contacts.append(tel)

    data.append({
        "titulo": title,
        "descricao": describe,
        "preco": extract_number(price),
        "condominio": extract_number(cond),
        "iptu": extract_number(iptu),
        "area": area,
        "quartos": bedroom,
        "banheiro": bathroom,
        "vagas": garage,
        "suite": suites,
        "outros": others,
        "address": address,
        "telefone": contacts,                 # ERRO
        "mobiliaria": mobi,                     # ERRO
        "url_mobiliaria": url_mobi,
        "images": image_urls,
        "data_criacao_anuncio": create_dt,
        "data_atualizacao_anuncio": update_dt
    })

    scraper.close_driver()

pd.DataFrame.from_dict(data).to_csv(
    "scr/scraper/info_imoveis.csv",
    index=False
)
