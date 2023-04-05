from enum import Enum
import random


class Cartes:

    paquet = []

    def __init__(self):
        self.paquet = [n for n in range(1, 55)]

    def __repr__(self) -> str:
        return str(self.paquet)

    def __str__(self) -> str:
        strPaquet = ""
        for carte in self.paquet:
            strPaquet += self.num2card(carte) + " "
        return strPaquet

    def __eq__(self, other):
        return self.paquet == other.paquet

    def __ne__(self, other):
        return self.paquet != other.paquet

    def melanger(self, seed=0):
        if (seed != 0):
            random.seed(seed)
        random.shuffle(self.paquet)

    @staticmethod
    def eval(strPaquet):
        paquet = [int(carte) for carte in strPaquet.split(" ") if carte != ""]
        paquetTest = sorted(paquet)
        if paquetTest == [n for n in range(1, 55)]:
            cartes = Cartes()
            cartes.paquet = paquet
            return cartes
        else:
            return []

    @staticmethod
    def num2card(num):
        card = ""

        # Jokers
        if num == Joker.NOIR.value:
            return "J♠"
        if num == Joker.ROUGE.value:
            return "J♥"

        # Numéro de la carte
        if num % 13 == Tetes.ROI.value:
            card += "R"
        elif num % 13 == Tetes.AS.value:
            card += "A"
        elif num % 13 == Tetes.DAME.value:
            card += "V"
        elif num % 13 == Tetes.VALET.value:
            card += "D"
        else:
            card += str(num % 13)

        # Symbole de la carte
        if num//13 == Symboles.PIQUE.value:
            card += "♠"
        elif num//13 == Symboles.TREFLE.value:
            card += "♣"
        elif num//13 == Symboles.COEUR.value:
            card += "♥"
        elif num//13 == Symboles.CARREAU.value:
            card += "♦"

        return card

    # Déplace une carte d'une distance donnée dans le paquet.
    # Si la distance est positive, la carte est déplacée vers la droite.
    # Si la distance est négative, la carte est déplacée vers la gauche.
    # Le paquet est cyclique, donc si la carte est déplacée trop loin, elle revient au début.
    def deplacer(self, carte, distance):
        index = self.paquet.index(carte)
        if (index + distance) < 0 or (index + distance) > 53:
            distance += 1
        self.paquet.insert((index+distance) % 54, self.paquet.pop(index))

    # Double coupe intervertit les deux parties du paquet autour des deux cartes données, en incluant ces cartes.
    def double_coupe(self, carte1, carte2):
        index1 = self.paquet.index(carte1)
        index2 = self.paquet.index(carte2)
        if index1 > index2:
            index1, index2 = index2, index1
        self.paquet = self.paquet[index2+1:] + \
            self.paquet[index1:index2+1] + self.paquet[:index1]

    # Coupe du paquet déterminée par la dernière carte du paquet. Les deux jokers valent 53.
    # ATTENTION : La carte à la fin doit rester à la fin après la coupe.
    def coupe(self):
        carte = self.paquet[-1]
        if carte == Joker.NOIR.value or carte == Joker.ROUGE.value:
            carte = 53
        self.paquet = self.paquet[carte:53] + \
            self.paquet[:carte] + [self.paquet[-1]]

    # Génère un caractère de la clé de chiffrement à partir du paquet de cartes.
    def nextKey(self):
        while True:
            # Recul du joker noir d'une position
            self.deplacer(Joker.NOIR.value, 1)
            # Recul du joker rouge de deux positions
            self.deplacer(Joker.ROUGE.value, 2)
            # Double coupe autour des deux jokers
            self.double_coupe(Joker.NOIR.value, Joker.ROUGE.value)
            # Coupe du paquet déterminée par la dernière carte du paquet
            self.coupe()
            # Lecture de la carte à la position donnée par la valeur de la première carte du paquet.
            # Si la carte est un joker, on recommence.
            # Valeur modulo 26 pour obtenir un caractère de l'alphabet en majuscule.
            carte = self.paquet[self.paquet[0]-1]
            if carte != Joker.NOIR.value and carte != Joker.ROUGE.value:
                return chr((carte % 26) + 65)

    def nextKeyStream(self, length):
        keyStream = ""
        for i in range(length):
            keyStream += self.nextKey()
        return keyStream

    # ------------------ ENUMERATIONS ------------------


class Joker(Enum):
    NOIR = 53
    ROUGE = 54


class Symboles(Enum):
    TREFLE = 0
    CARREAU = 1
    COEUR = 2
    PIQUE = 3


class Tetes(Enum):
    ROI = 0
    AS = 1
    VALET = 11
    DAME = 12
