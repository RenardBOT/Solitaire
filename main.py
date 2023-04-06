# importer l'entièreté du fichier Solitaire.py
from Solitaire import *
import traceback

# Main fonction printant hello world
# 54 2 1 53 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 3


def main():
    paquet = Cartes()

    choix = input("Voulez-vous chiffrer ou déchiffrer un message ? (C/D) : ")
    saisie = input("Voulez vous générer un paquet de cartes aléatoirement ou le saisir? (G/S) : ")
    if saisie == "G" :
        graine = input(
            "Saisissez la graine de génération de la clé de chiffrement (0 par défaut) : ")
        if graine == "":
            graine = 0
        else:
            graine = int(graine)
        paquet.melanger(graine)
    else:
        while True:
            try:
                paquetStr = input(
                    "Saisissez un arrangement de chaque nombre compris entre 1 et 54. Les cartes sont ordonnées selon l'ordre du bridge, 53 et 54 sont les jokers noir et rouge : \n")
                paquet.set(Cartes.eval(paquetStr))
                break
            except:
                traceback.print_exc()
                continue
    
        
    verbose = input("Activer la verbosité? (Y/N) : ")
    if verbose == "Y": paquet.setVerbose(True)

    # Si l'utilisateur veut chiffrer un message
    if choix == "C":
        message = input("Saisissez le message à chiffrer : ")
        print("Message nettoyé : " + nettoyerMessage(message))
        
        print("Paquet de cartes initial :")
        print(paquet)
        key = paquet.nextKeyStream(len(message))
        print("Le message chiffré est : " + chiffrer(message, key))

    # Si l'utilisateur veut déchiffrer un message
    else:
        message = input("Saisissez le message à déchiffrer : ")
        print("Message nettoyé : " + nettoyerMessage(message))
        print("Paquet de cartes :")
        print(paquet)
        key = paquet.nextKeyStream(len(message))
        print("Le message déchiffré est : " + dechiffrer(message, key))


if __name__ == "__main__":
    main()
