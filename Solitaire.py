# importation de Cartes.py et de la librairie re
from Cartes import Cartes
import re


def chiffrer(message, key):
    message = nettoyerMessage(message)
    # Additionne le message et la clé
    result = ""
    for i in range(len(message)):
        result += chr((ord(message[i]) + ord(key[i])+1) % 26+65)
    return result


def dechiffrer(message, key):
    message = nettoyerMessage(message)
    # Soustrait le message et la clé
    result = ""
    for i in range(len(message)):
        result += chr((ord(message[i]) - ord(key[i])-1) % 26+65)
    return result


# Pour que le message soit valide, on ne garde que les lettres, et on convertit les minuscules en majuscules
def nettoyerMessage(message):
    message = message.upper()
    message = re.sub(r'[^A-Z]', '', message)
    return message
