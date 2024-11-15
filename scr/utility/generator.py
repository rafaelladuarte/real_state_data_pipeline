from br_nome_gen import pessoa_random
from unidecode import unidecode   # type: ignore

import random


def generator_phone():
    digit = ["9"]
    phone = []
    for i in range(0, 7):
        digit += str(random.randint(0, 9))
    phone = "34" + ''.join(digit)
    return phone


def generator_name():
    return pessoa_random().nome


def generator_email(nome):
    name_sem_acento = unidecode(nome.lower())

    parts_name = name_sem_acento.split()
    first_name = parts_name[0]
    last_name = parts_name[-1]

    dominios = ['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com']
    random_number = random.randint(10, 999)

    option_email = [
        f"{first_name}.{last_name}{random_number}@{dominios[0]}",
        f"{first_name}{random_number}@{dominios[0]}",
        f"{first_name}_{last_name}@{dominios[0]}",
        f"{first_name}{last_name}{random_number}@{dominios[0]}",
        f"{first_name}.{last_name}{random_number}@{dominios[1]}",
        f"{first_name}{random_number}@{dominios[1]}",
        f"{first_name}_{last_name}@{dominios[1]}",
        f"{first_name}{last_name}{random_number}@{dominios[1]}",
        f"{first_name}.{last_name}{random_number}@{dominios[2]}",
        f"{first_name}{random_number}@{dominios[2]}",
        f"{first_name}_{last_name}@{dominios[2]}",
        f"{first_name}{last_name}{random_number}@{dominios[2]}",
        f"{first_name}.{last_name}{random_number}@{dominios[3]}",
        f"{first_name}{random_number}@{dominios[3]}",
        f"{first_name}_{last_name}@{dominios[3]}",
        f"{first_name}{last_name}{random_number}@{dominios[3]}",
    ]

    return random.choice(option_email)


def generator_creci():
    list_uf = [
        "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA",
        "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN",
        "RS", "RO", "RR", "SC", "SP", "SE", "TO"
    ]

    number_creci = random.randint(10000, 99999)
    uf_creci = random.choice(list_uf)

    creci = f"CRECI {number_creci}-{uf_creci}"

    return creci
