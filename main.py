import re

def recherche(mot, chaine):
    match = re.search(mot, chaine)
    return bool(match)

def verifie_chaine(chaine):
    match = re.search(r"\d", chaine)
    return bool(match)

def remplace(chaine):
    return re.sub(r"\s", "-", chaine)

def verifie_numero(numero):
    match = re.search(r"^\d{2}-\d{3}-\d{4}$", numero)
    return bool(match)

def verifie_email(email):
    match = re.search(r"^\w+@\w+\.(com|ma|org|info|ru)$", email)
    return bool(match)
