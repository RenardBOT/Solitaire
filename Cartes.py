from enum import Enum
import random


class Cartes:

    paquet = []
    verbose = False

    def __init__(self):
        self.paquet = [n for n in range(1, 55)]

    def __repr__(self):
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
    
    def setVerbose(self,verbose):
        self.verbose = verbose

    def melanger(self, seed=0):
        if (seed != 0):
            random.seed(seed)
        random.shuffle(self.paquet)

    def set(self,paquet):
        paquetTest = sorted(paquet)
        if paquetTest != [n for n in range(1,55)]:
            raise InvalidDeck
        self.paquet = paquet
        

    # exemple paquet : 54 2 1 53 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 3

    @staticmethod
    def eval(strPaquet):
        paquet = [int(carte) for carte in strPaquet.split(" ") if carte != ""]
        return paquet

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
            card += "D"
        elif num % 13 == Tetes.VALET.value:
            card += "V"
        else:
            card += str(num % 13)

        # Symbole de la carte
        if (num-1)//13 == Symboles.PIQUE.value:
            card += "♠"
        elif (num-1)//13 == Symboles.TREFLE.value:
            card += "♣"
        elif (num-1)//13 == Symboles.COEUR.value:
            card += "♥"
        elif (num-1)//13 == Symboles.CARREAU.value:
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
        if self.verbose : print("----------- GENERATION CARACTERE DE LA CLEF")
        while True:
            # Recul du joker noir d'une position
            self.deplacer(Joker.NOIR.value, 1)
            # Recul du joker rouge de deux positions
            self.deplacer(Joker.ROUGE.value, 2)
            if self.verbose : print("| Recul des jokers : " + str(self))
            # Double coupe autour des deux jokers
            self.double_coupe(Joker.NOIR.value, Joker.ROUGE.value)
            if self.verbose : print("| Double coupe autour des jokers : " + str(self))
            # Coupe du paquet déterminée par la dernière carte du paquet
            self.coupe()
            if self.verbose : print("| Coupe en fonction de la dernière carte : " + str(self))
            # Lecture de la carte à la position donnée par la valeur de la première carte du paquet.
            # Si la carte est un joker, on recommence.
            # Valeur modulo 26 pour obtenir un caractère de l'alphabet en majuscule.
            pioche = self.paquet[0]-1
            carte = self.paquet[pioche]
            if pioche != Joker.NOIR.value and carte != Joker.ROUGE.value:
                lettre = chr((carte % 26) + 65)
                if self.verbose : print("| La valeur de la première carte correspond à la lettre [" + lettre + "]")
                return lettre
            else:
                if self.verbose : print("---- La première carte est un Joker. Nouvel essai ")

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

class InvalidDeck(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
        message -- explanation of the error
    """
    #"ERREUR : Le paquet doit être un arrangement de chaque nombre compris entre 1 et 54"
    def __init__(self, message="Le paquet doit être un arrangement de chaque nombre compris entre 1 et 54"):
        self.message = message
        super().__init__(self.message)
    pass
