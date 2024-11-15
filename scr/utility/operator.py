import re
from datetime import datetime, timedelta
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')


def extract_date(frase):
    date_created, date_updated = None, None
    if frase:
        defautl_created = r"criado em (\d{1,2} de \w+ de \d{4})"
        match_created = re.search(defautl_created, frase)

        defautl_since = r"Desde (\d{1,2} de \w+ de \d{4})"
        match_since = re.search(defautl_since, frase)

        defautl_updated = r"há (\d+) dias"
        match_updated = re.search(defautl_updated, frase)

        if match_created:
            date_created = datetime.strptime(
                match_created.group(1),
                "%d de %B de %Y"
            ).date()

            date_created = date_created.strftime("%d/%m/%Y")
        elif match_since:
            date_created = datetime.strptime(
                match_since.group(1),
                "%d de %B de %Y"
            ).date()
            date_created = date_created.strftime("%d-%m-%Y %H:%M:%S")

        if match_updated:
            days_ago = int(match_updated.group(1))
            date_updated = datetime.now().date() - timedelta(days=days_ago)
            date_updated = date_updated.strftime("%d-%m-%Y %H:%M:%S")

    return date_created, date_updated


def extract_number(text):
    if text:
        text = re.sub(r'(?<=\d)\.(?=\d{3}(?:\D|$))', '', text)
        text = text.replace(',', '.')

        padrao = re.compile(r'\d+\.\d+|\d+')
        numeros_encontrados = re.findall(padrao, text)

        numeros = [
            float(num)
            if '.' in num else int(num)
            for num in numeros_encontrados
        ]

        return numeros if len(numeros) > 1 else numeros[0] if numeros else None


def treatment_string(text):

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


if __name__ == '__main__':
    test_cases = [
        '3 banheiro',
        'R$ 280.000',
        'R$ 1.800.000,00',
        '45,67',
        '1.234,56',
        'https://www.zapimoveis.com.br/imobiliaria/734810/',
        'O número é 12345 na URL',
        'Aqui temos um número decimal: 123.45 e outro 6.789',
    ]

    for case in test_cases:
        result = extract_number(case)
        print(f"'{case}' -> {result}")
