from selenium.webdriver.common.by import By
from scraper import WebScraper
from utility import (
    gerador_email, gerador_nome, gerador_telefone
)

import pandas as pd
import csv


links = []
with open("scraper/links.csv", encoding='utf-8') as csvf:
    reader = csv.reader(csvf)
    next(reader, None)
    for row in reader:
        links.append(row[0])

data = []
for link in links:
    scraper = WebScraper()
    scraper.get_driver(link)

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
    amenities = scraper.get_element(
        by=By.CLASS_NAME,
        path="amenities-list",
        driver_element=details
    )
    span_item = 'span[contains(@class, "amenities-item-text")]'

    area = scraper.get_element(
        by=By.XPATH,
        path=f'//p[@itemprop="floorSize"]//{span_item}',
        attribute_type="text",
        driver_element=amenities
    )
    quarto = scraper.get_element(
        by=By.XPATH,
        path=f'//p[@itemprop="numberOfRooms"]//{span_item}',
        attribute_type="text",
        driver_element=amenities
    )
    banheiro = scraper.get_element(
        by=By.XPATH,
        path=f'//p[@itemprop="numberOfBathroomsTotal"]//{span_item}',
        attribute_type="text",
        driver_element=amenities
    )
    vagas = scraper.get_element(
        by=By.XPATH,
        path=f'//p[@itemprop="numberOfParkingSpaces"]//{span_item}',
        attribute_type="text",
        driver_element=amenities
    )
    suites = scraper.get_element(
        by=By.XPATH,
        path=f'//p[@itemprop="numberOfSuites"]//{span_item}',
        attribute_type="text",
        driver_element=amenities
    )
    outras = {}

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

    # PREENCHENDO FORMULARIO DE COLETA DE TELEFONE

    nome_gerado = gerador_nome()
    phone_gerado = gerador_telefone()
    email_gerado = gerador_email(nome_gerado)

    forms = scraper.get_element(
        by=By.CLASS_NAME,
        path="form-lead-container"
    )

    nome = scraper.get_element(
        by=By.ID,
        path='l-input-7',
        # driver_element=forms
    )
    nome.send_keys(nome_gerado)

    email = scraper.get_element(
        by=By.ID,
        path='l-input-8',
        # driver_element=forms
    )
    email.send_keys(email_gerado)

    phone = scraper.get_element(
        by=By.ID,
        path='l-input-9',
        # driver_element=forms
    )
    phone.send_keys(phone_gerado)

    scraper.get_element(
        by=By.ID,
        path="adopt-accept-all-button",
        attribute_type="button"
    )   # Botão para fechar modal de cookies

    # XPATH
    # "//button[@data-testid='l-button' and
    #       @data-cy='ldp-formMessage-sendMessage-btn']"]
    # CSS SELECTOR
    # "button[data-testid='l-button']
    #       [data-cy='ldp-formMessage-sendMessage-btn']"
    # CLASS NAME'
    # 'l-button l-button--context-secondary
    #       l-button--size-regular l-button--icon-left'

    scraper.get_element(
        by=By,
        path="",
        attribute_type="button",
        driver_element=forms
    )   # Botão para enviar formulario

    # COLETA DA LISTA DE TELEFONES
    list_phone = scraper.get_element(
        by=By.XPATH,
        path="//button[@data-cy='lead-modalPhone-phonesList-txt']",
        attribute_type="href"
    )

    # COLETA DA DATA DE CRIAÇÃO DO ANUNCIO
    create_update = scraper.get_element(
        by=By.CSS_SELECTOR,
        path="span[data-testid='listing-created-date']",
        attribute_type="text",
        driver_element=details,
    )

    data.append({
        "titulo": title,
        "descricao": describe,
        "preco": price,
        "condominio": cond,
        "iptu": iptu,
        "area": area,
        "quartos": quarto,
        "banheiro": banheiro,
        "vagas": vagas,
        "suite": suites,
        "outros": outras,
        "address": address,
        "telefone": list_phone,
        "mobiliaria": mobi,
        "url_mobiliaria": url_mobi,
        "data_criacao_anuncio": create_update
    })

    scraper.close_driver()

pd.DataFrame.from_dict(data).to_csv(
    "scraper/info_imoveis.csv",
    index=False
)
