# -*- coding:utf-8 -*-
# MIT OpenCourseWare
# Word Game

import random
import string

# Global Constants
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

HUMAN_SOLO = 0
HUMAN_VS_HUMAN = 1
HUMAN_VS_COMP = 2

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Regresa todas las palabras válidas que se usarán para la partida,
    todas conformadas por letras minúsculas.

    El archivo words.txt es el que contiene las palabras validas.
    """

    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    return wordlist

def getFrequencyDict(sequence):
    """
    Regresa un diccionario donde las claves son letras de la partida
    y los valores son los recuentos, el numero de veces que un elemento
    es repetido en la partida.

    sequence: string or list
    return: dictionary
    """

    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

def getWordScore(word, n):
    """
    Regresa el score para cada palabra, asumiendo que la palabra es valida.

    El score para cada palabra es la suma de los puntos de cada letra
    en la palabra, más 50 puntos si todas las letras son utilizadas.

    Los valores de cada letras son como en el Scrabble y están almacenadas
    en el diccionario SCRABBLE_LETTER_VALUES.

    word: string (lowercase letters)
    returns: int >= 0
    """

    total = 0

    # Hace la comparación del string recibido con el diccionario de valores para obtener el total.
    for key in word:
        if key in SCRABBLE_LETTER_VALUES:
            value = SCRABBLE_LETTER_VALUES[key]

        total = total + value

    if len(word) == n:
        total += 50
    return total

#
# Problem 2: Representing a Hand
#

class Hand(object):

    def __init__(self, handSize, initialHandDict = None):
        """
        Inicializa una mano.
        handSize: El tamaño de letras de la jugada
        postcondition: Inicializa una mano con un set random de letras iniciales
        """

        num_vowels = round(handSize / 3)
        if initialHandDict is None:
            initialHandDict = {}
            for i in range(num_vowels):
                x = VOWELS[random.randrange(0, len(VOWELS))]
                initialHandDict[x] = initialHandDict.get(x, 0) + 1
            for i in range(num_vowels, handSize):
                x = CONSONANTS[random.randrange(0, len(CONSONANTS))]
                initialHandDict[x] = initialHandDict.get(x, 0) + 1

        self.initialSize = handSize
        self.hand = initialHandDict

    def update(self, word):
        """
        Remueve las letras de la mano que fueron usadas en la palabra.

        word: La palabra (a string) para remover de la mano.
        postcondition: Letters in word are removed from this hand
        """

        # Busca cada letra de la palabra en el diccionario y le va restando una unidad a la cantidad de veces que
        # aparece la letra

        for letter in word:
            if letter in self.hand:
                self.hand[letter] = self.hand[letter] - 1
                if self.hand[letter] == 0:
                    del self.hand[letter]

        return self.hand

    def containsLetters(self, letters):
        """
        Testea si la mano contiene los caracteres requeridos para hacer el input string (letters)

        returns: Verdadero si la mano contiene los caracteres de la palabra
        False otherwise
        """

        for character in letters:
            if character in self.hand:
                valid = True
            else:
                return False

        if valid:
            return True

    def isEmpty(self):
        """
        Testea si hay alguna letra en la mano

        returns: True if there are no letters remaining, False otherwise.
        """

        if self.hand == {}:
            return True
        else:
            return False

    def __eq__(self, other):
        """
        Test de igualdad, para propositos de testing

        returns: Verdadero si la mano contiene el mismo numero de cada letras comparado con otra mano, de otra forma es
        False
        """

        if self.hand == other:
            return True
        else:
            return False

    def __str__(self):
        """
        Representa la mano como un string

        returns: a string representation of this hand
        """

        finalhand = ""

        for letter in self.hand.keys():
            for j in range(self.hand[letter]):
                finalhand = finalhand + letter + " " # Almacena letra por letra para mostrarlo de forma horizontal

        return finalhand

#
# Problem 3: Representing a Player
#

class Player(object):
    """
    Clase general que describe a un jugador. Almacena su ID, su juego y score.
    """
    def __init__(self, idNum, hand):
        """
        Inicializa el jugador

        idNum: integer: 1 for player 1, 2 for player 2.  Used in informational
        displays in the GUI.

        hand: An object of type Hand.

        postcondition: This player object is initialized
        """
        self.score = 0
        self.idNum = idNum
        self.hand = hand

    def getHand(self):
        """
        Regresa la mano del jugador.

        returns: la mano asociada con el jugador.
        """

        return self.hand

    def addPoints(self, points):
        """
        Añade puntos al score total del jugador.

        points: el numero de puntos añadidos al score del jugador

        postcondition: el score total del jugador es incrementado por los puntos
        """

        self.score += points
        return "Añadidos {} puntos.".format(points)

    def getScore(self):
        """
        Regresa el score total del jugador

        returns: Un entero especificando el player score
        """
        return self.score

    def getIdNum(self):
        """
        Regresa el ID number del jugador, 1 para el jugador 1, 2 para el jugador 2.

        returns: Un entero especificando el player ID
        """

        return self.idNum

    def __lt__(self, other):
        """
        Compara los jugadores por sus scores.

        returns: 1 si el score del jugador es mayor al del otro, -1 si es el score del jugador es menor que el otro y 0
        si son iguales.
        """

        if self.score < other.score:
            return 1
        elif self.score > other.score:
            return -1

    def __eq__(self, other):

        if self.score == other.score:
            return 0
        else:
            return False

    def __str__(self):
        """
        Representa este jugador como un string

        returns: a string representation of this player
        """
        return "Jugador {}. Score: {}".format(self.getIdNum(), self.getScore())