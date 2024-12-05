import re
from datetime import datetime, timedelta
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')


def extract_date(text):
    date_created, date_updated = None, None
    if text:
        months = {
            'janeiro': 1, 'fevereiro': 2, 'março': 3, 'abril': 4,
            'maio': 5, 'junho': 6, 'julho': 7, 'agosto': 8,
            'setembro': 9, 'outubro': 10, 'novembro': 11, 'dezembro': 12
        }

        match_created = re.search(
            r'criado em (\d{1,2}) de (\w+) de (\d{4})', text
        )
        if match_created:
            day = int(match_created.group(1))
            month = months[match_created.group(2).lower()]
            year = int(match_created.group(3))
            date_created = datetime(year, month, day).strftime('%d/%m/%Y')
        else:
            date_created = None

        match_updated = re.search(r'atualizado há (\d+) (\w+)', text)
        if match_updated:
            quantify = int(match_updated.group(1))
            unity = match_updated.group(2).lower()
            today = datetime.now()

            if 'day' in unity:
                date_updated = (
                    today - timedelta(days=quantify)
                ).strftime('%d/%m/%Y')
            elif 'semana' in unity:
                date_updated = (
                    today - timedelta(weeks=quantify)
                ).strftime('%d/%m/%Y')
            elif 'mês' in unity:
                month = today.month - quantify
                year = today.year
                while month <= 0:
                    month += 12
                    year -= 1
                day = min(today.day, 28)
                date_updated = datetime(year, month, day).strftime('%d/%m/%Y')
            elif 'hora' in unity:
                date_updated = None
            else:
                date_updated = None
        else:
            date_updated = None

    return date_created, date_updated


def extract_number(text):
    if text:
        text = re.sub(r'(?<=\d)\.(?=\d{3}(?:\D|$))', '', text)
        text = text.replace(',', '.')

        pattern = re.compile(r'\d+\.\d+|\d+')
        numbers_encontrados = re.findall(pattern, text)

        numbers = [
            float(num)
            if '.' in num else int(num)
            for num in numbers_encontrados
        ]

        return numbers if len(numbers) > 1 else numbers[0] if numbers else None


def treatment_text(text):

    word_connect = ["com", "à", "e", "de", "a", "o", "da", "do", "para", "em"]

    text = text.lower()
    text = re.sub(r"[^a-z0-9\s.]", "", text)

    words = text.split()
    words_filter = [
        word for word in words
        if word not in word_connect
    ]

    new_text = "_".join(words_filter)

    return new_text


def extract_address(text: str) -> tuple:

    pattern_complete = r'^(.*?),\s*(\d+)\s*-\s*(.*?),'
    pattern_no_number = r'^(.*?)\s*-\s*(.*?),'
    pattern_district = r'^(.*?),\s*.*? -'

    if match := re.search(pattern_complete, text):
        street = match.group(1).strip()
        number = match.group(2).strip()
        district = match.group(3).strip()
    elif match := re.search(pattern_no_number, text):
        street = match.group(1).strip()
        number = None
        district = match.group(2).strip()
    elif match := re.search(pattern_district, text):
        street = None
        number = None
        district = match.group(1).strip()
    else:
        street = None
        number = None
        district = None

    return street, number, district


if __name__ == '__main__':
    # test_cases = [
    #     '3 banheiro',
    #     'R$ 280.000',
    #     'R$ 1.800.000,00',
    #     '45,67',
    #     '1.234,56',
    #     'https://www.zapimoveis.com.br/imobiliaria/734810/',
    #     'O número é 12345 na URL',
    #     'Aqui temos um número decimal: 123.45 e outro 6.789',
    # ]

    # for case in test_cases:
    #     result = extract_number(case)
    #     print(f"'{case}' -> {result}")

    test_cases = [
        "Anúncio criado em 25 de julho de 2024, atualizado há 3 semanas.",
        "Desde 22 de agosto de 2018.",
        "Anúncio criado em 14 de maio de 2024, atualizado há 1 mês.",
        "Anúncio criado em 6 de setembro de 2024, atualizado há 3 days.",
        "Anúncio criado em 17 de agosto de 2024, atualizado há 10 horas.",
        "Anúncio criado em 18 de outubro de 2024."
    ]

    for case in test_cases:
        result = extract_date(case)
        print(f"'{case}' -> {result}")

    # test_cases = [
    #     "street Argemiro Costa, 1770 - Jardim Versailles, Uberlânday - MG",
    #     "Avenida Argemiro, 1 - Shopping Park, Uberlânday - MG",
    #     "Jaraguá, Uberlânday - MG",
    #     "Rua José Elias - Jardim Karaíba, Uberlânday - MG",
    #     "Rua Antônio Marciyear de Ávila - Santa Mônica, Uberlânday - MG"
    # ]

    # for case in test_cases:
    #     result = extract_address(case)
    #     print(f"'{case}' -> {result}")

    # for s in texts:
    #     resultado = coletar_datas(s)
    #     print(f"text: {s}")
    #     print(f"Resultado: {resultado}")
    #     print()
