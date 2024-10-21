from br_nome_gen import pessoa_random

from unidecode import unidecode   # type: ignore
import random


def gerador_telefone():
    digitos = ["9"]
    telefone = []
    for i in range(0, 7):
        digitos += str(random.randint(0, 9))
    telefone = "34" + ''.join(digitos)
    return telefone


def gerador_nome():
    return pessoa_random().nome


def gerador_email(nome):
    nome_sem_acento = unidecode(nome.lower())

    partes_nome = nome_sem_acento.split()
    primeiro_nome = partes_nome[0]
    ultimo_nome = partes_nome[-1]

    dominios = ['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com']
    numero_aleatorio = random.randint(10, 999)

    opcoes_email = [
        f"{primeiro_nome}.{ultimo_nome}{numero_aleatorio}@{dominios[0]}",
        f"{primeiro_nome}{numero_aleatorio}@{dominios[0]}",
        f"{primeiro_nome}_{ultimo_nome}@{dominios[0]}",
        f"{primeiro_nome}{ultimo_nome}{numero_aleatorio}@{dominios[0]}",
        f"{primeiro_nome}.{ultimo_nome}{numero_aleatorio}@{dominios[1]}",
        f"{primeiro_nome}{numero_aleatorio}@{dominios[1]}",
        f"{primeiro_nome}_{ultimo_nome}@{dominios[1]}",
        f"{primeiro_nome}{ultimo_nome}{numero_aleatorio}@{dominios[1]}",
        f"{primeiro_nome}.{ultimo_nome}{numero_aleatorio}@{dominios[2]}",
        f"{primeiro_nome}{numero_aleatorio}@{dominios[2]}",
        f"{primeiro_nome}_{ultimo_nome}@{dominios[2]}",
        f"{primeiro_nome}{ultimo_nome}{numero_aleatorio}@{dominios[2]}",
        f"{primeiro_nome}.{ultimo_nome}{numero_aleatorio}@{dominios[3]}",
        f"{primeiro_nome}{numero_aleatorio}@{dominios[3]}",
        f"{primeiro_nome}_{ultimo_nome}@{dominios[3]}",
        f"{primeiro_nome}{ultimo_nome}{numero_aleatorio}@{dominios[3]}",
    ]

    return random.choice(opcoes_email)
