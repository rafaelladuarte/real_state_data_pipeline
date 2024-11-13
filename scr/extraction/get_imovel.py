from selenium.webdriver.common.by import By

from security.secrets import get_secret_value
from storage.mongo import MongoDB
from scraper import WebScraper

from utility.generator import (
    generator_email, generator_name, generator_phone
)
from utility.operator import (
    extract_date, extract_number
)

from datetime import datetime
from time import sleep

mongo = MongoDB(
    uri=get_secret_value('MONGO_URI')
)

docs = mongo.get_documents(
    flag='scraper',
    database='scraper',
    collection='links_imoveis'
)

data = []
list_id = []
for doc in docs[:10]:
    link = doc['link']
    list_id.append(doc['id'])

    scraper = WebScraper()
    scraper.get_driver(link)

    # COLETA DADOS DO ANUNCIO
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

    # COLETA LINK DAS IMAGENS
    carousel_images = scraper.get_elements(
        by=By.XPATH,
        path="//ul[@class='carousel-photos--wrapper']/li"
    )

    original_image_urls = []
    for li in carousel_images:
        srcset = scraper.get_element(
            by=By.CLASS_NAME,
            path="carousel-photos--img",
            attribute_type="srcset",
            driver_element=li
        )
        if srcset:
            largest_image_url = srcset.split(",")[-1].strip().split(" ")[0]
            original_image_urls.append(largest_image_url)

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
        "endereco": address,
        "telefone": contacts,                   # ERRO
        "imobiliaria_id": extract_number(url_mobi),
        "original_imagens": original_image_urls,
        "data_criacao_anuncio": create_dt,
        "data_atualizacao_anuncio": update_dt,
        "created_dt": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    })

    scraper.close_driver()

mongo.update_documents(
    ids=list_id,
    flag="scraper",
    database='scraper',
    collection='links'
)

mongo.insert_documents(
    documents=data,
    database='scraper',
    collection='imoveis'
)