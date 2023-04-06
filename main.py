# importer l'entièreté du fichier Solitaire.py
from Solitaire import *

# Main fonction printant hello world


def main():
    # Offre un choix à l'utilisateur entre l'option chiffrement et déchiffrement
    choix = input("Voulez-vous chiffrer ou déchiffrer un message ? (C/D) : ")
    # Offre le choix de la graine de génération de la clé de chiffrement. Si l'utilisateur ne saisit rien, la graine est 0.
    graine = input(
        "Saisissez la graine de génération de la clé de chiffrement (0 par défaut) : ")
    if graine == "":
        graine = 0
    else:
        graine = int(graine)
    verbose = input("Activer la verbosité? (Y/N) : ")

    if verbose == "Y":
        verbose = True
    else:
        verbose = False

    # Si l'utilisateur veut chiffrer un message
    if choix == "C":
        message = input("Saisissez le message à chiffrer : ")
        print("Message nettoyé : " + nettoyerMessage(message))
        paquet = Cartes()
        paquet.setVerbose(verbose)
        paquet.melanger(graine)
        print("Paquet de cartes initial :")
        print(paquet)
        key = paquet.nextKeyStream(len(message))
        print("Le message chiffré est : " + chiffrer(message, key))

    # Si l'utilisateur veut déchiffrer un message
    elif choix == "D":
        message = input("Saisissez le message à déchiffrer : ")
        print("Message nettoyé : " + nettoyerMessage(message))
        paquet = Cartes()
        paquet.setVerbose(verbose)
        paquet.melanger(graine)
        print("Paquet de cartes :")
        print(paquet)
        key = paquet.nextKeyStream(len(message))
        print("Le message déchiffré est : " + dechiffrer(message, key))


if __name__ == "__main__":
    main()
