import re
from datetime import datetime, timedelta
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')


def extract_date(frase):
    defautl_created = r"criado em (\d{1,2} de \w+ de \d{4})"
    match_created = re.search(defautl_created, frase)

    if match_created:
        date_created = datetime.strptime(
            match_created.group(1),
            "%d de %B de %Y"
        ).date()
        date_created.strftime("%d/%m/%Y")
    else:
        date_created = None

    defautl_updated = r"há (\d+) dias"
    match_updated = re.search(defautl_updated, frase)

    if match_updated:
        days_ago = int(match_updated.group(1))
        date_updated = datetime.now().date() - timedelta(days=days_ago)
        date_updated.strftime("%d/%m/%Y")
    else:
        date_updated = None

    return date_created,  date_updated


def extract_number(word):
    number = re.findall("[0-9]+", word)
    if len(number) > 0:
        return number[0]

    return None
