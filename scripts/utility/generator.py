from br_nome_gen import pessoa_random
from unidecode import unidecode   # type: ignore

import random


def generator_phone() -> str:
    digit = ["9"]
    phone = []
    for i in range(0, 7):
        digit += str(random.randint(0, 9))
    phone = "34" + ''.join(digit)
    return phone


def generator_name() -> str:
    return pessoa_random().nome


def generator_email(name: str) -> str:
    name_sem_acento = unidecode(name.lower())

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
