import random


def updateDict(list, dict):
    dict.clear()
    for index, value in enumerate(list):
        dict[value] = index


def swap(list, val1, val2):
    list[val1], list[val2] = list[val2], list[val1]


# ------------------ MAIN ------------------

lenMessage = 15
iter = 0
cle = ""

while (iter < lenMessage):
    cartes = [n for n in range(1, 55)]
    random.shuffle(cartes)

    dict = {}

    updateDict(cartes, dict)

    jokerNoir, jokerRouge = dict[53], dict[54]
    swap1, swap2 = (jokerNoir+1) % 54, (jokerRouge+2) % 54

    cartes[jokerNoir], cartes[swap1] = cartes[swap1], cartes[jokerNoir]
    updateDict(cartes, dict)
    cartes[jokerRouge], cartes[swap2] = cartes[swap2], cartes[jokerRouge]
    updateDict(cartes, dict)
    jokerNoir, jokerRouge = dict[53], dict[54]

    coupeDebut = cartes[:jokerNoir]
    coupeMilieu = cartes[jokerNoir:jokerRouge+1]
    coupeFin = cartes[jokerRouge+1:]

    # Concatene les trois listes dans une variable et affiche le jeu complet
    cartes = coupeFin + coupeMilieu + coupeDebut

    coupeFin = cartes[-1]
    if coupeFin == 54:
        coupeFin = 53
    coupeDebut = cartes[:coupeFin]
    coupeMilieu = cartes[coupeFin:-1]

    # Concatene les trois listes dans une variable et affiche le jeu complet
    cartes = coupeMilieu + coupeDebut + [coupeFin]

    if (cartes[0] == 53 or cartes[0] == 54):
        print("Joker présent")
        continue

    val = cartes[0] % 26
    cle += chr(val+65)
    iter += 1


# Crée un string message de 15 lettres sans espace en majuscule
message = "TOTSUGEKIPLOPOK"

# Aditionne clé et message
result = ""
for i in range(len(message)):
    result += chr((ord(message[i]) + ord(cle[i])+1) % 26+65)

print("Message : ", message)
print("Cle : ", cle)
print("Result : ", result)
