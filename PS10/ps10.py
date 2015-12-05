# -*- coding:utf-8 -*-
# MIT OpenCourseWare
# Word Game

import random
from itertools import permutations
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

def getWordScore(word):
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

    if len(word) == HAND_SIZE:
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
        self.index = 0

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

    def getHand(self):
        """
        Regresa la mano del jugador.

        returns: la mano asociada con el jugador.
        """

        return self.hand

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
        return "Jugador {} \n Score: {}".format(self.getIdNum(), self.getScore())

#
# Problem 4: Representing a Computer Player
#

class ComputerPlayer(Player):
    """
    Computer player class.
    Hace todo lo que el jugador hace, con la excepción de utiliza el método PickBestwWord
    """

    def __init__(self, idNum, hand):
        Player.__init__(self, idNum, hand)
        self.pointsdict = {}
        self.getWordsToPoints()

    def getWordsToPoints(self):
        """
        Regresa un diccionario que contiene todas las palabras con sus respectivos puntajes
        """

        # Toma cada palabra en la lista y forma un diccionario con la palabra y sus puntos equivalentes

        wordlist = Wordlist()

        for word in wordlist.getList():
            score = getWordScore(word)
            self.pointsdict.update({word: score})

        return self.pointsdict

    def getPossibleWord(self):
        """
        Esta función toma el hand de letras y regresa una lista de palabras posibles.

        returns: a list of possible words
        """

        finalhand = ''
        pw = {}
        hand = self.hand.getHand()

        for letter in hand:
            for j in range(hand[letter]):
                finalhand = finalhand + letter

        for L in range(2, len(finalhand)+1):
            for subset in permutations(finalhand, L):
                word = ''.join(subset)
                # print(word)
                pw.update({word: word})

        return pw

    def pickBestWord(self, possibleword):
        """
        Recibe dos diccionarios y revisa cuales palabras son posibles y regresa el valor mas alto que se puede obtener con la mano dada

        hand: dictionary
        possibleword: dictionary
        """

        bestword = ''
        bestwordvalue = 0

        words = possibleword.values()
        for word in words:
            if word in self.pointsdict:
                wordvalue = self.pointsdict[word]
                if wordvalue > bestwordvalue:
                    # print(word)
                    bestwordvalue = self.pointsdict[word]
                    bestword = word

        if bestwordvalue > 0:
            # print(bestword, bestwordvalue)
            return bestword

        return '.'

    def playHand(self, callback, wordlist):
        """
        Juega una mano, pasando las palabras elegidas a la función de llamada.
        """
        pw = self.getPossibleWord()
        while callback(self.pickBestWord(pw)):
            pass

class Wordlist(object):
    """
    A word list.
    """
    def __init__(self):
        """
        Initializes a Wordlist object.

        postcondition: words are read in from a file (WORDLIST_FILENAME, a
        global constant) and stored as a list.
        """
        inputFile = open(WORDLIST_FILENAME)
        try:
            self.wordlist = []
            for line in inputFile:
                self.wordlist.append(line.strip().lower())
        finally:
            inputFile.close()

    def containsWord(self, word):
        """
        Testea que la wordlist contiene la palabra

        word: The word to check (a string)

        returns: Verdadero si la palabra está en la wordlist, Falso si no
        """
        return word in self.wordlist

    def getList(self):
        return self.wordlist

class EndHand(Exception): pass

class Game(object):
    """
    Almacena el estado necesatio para jugar una ronda de word game
    """
    def __init__(self, mode, wordlist):
        """
        Inicializa un juego.

        mode: Se pueden tener 3 valores: - HUMAN_SOLO, HUMAN_VS_COMP and HUMAN_VS_HUMAN

        postcondition: Initializes the players and their hands.
        """
        hand = Hand(HAND_SIZE)
        hand2 = Hand(HAND_SIZE, hand.hand.copy())
        if mode == HUMAN_SOLO:
            self.players = [Player(1, hand)]
        elif mode == HUMAN_VS_COMP:
            self.players = [Player(1, hand),
                            ComputerPlayer(2, hand2)]
        elif mode == HUMAN_VS_HUMAN:
            self.players = [Player(1, hand),
                            Player(2, hand2)]
        self.playerIndex = 0
        self.wordlist = wordlist

    def getCurrentPlayer(self):
        """
        Obtieene el objeto Player de acuerdo al player activo.

        returns: The active Player object.
        """
        return self.players[self.playerIndex]

    def nextPlayer(self):
        """
        Cambia el estado del juego, entonces el siguiente jugador es el player activo.

        postcondition: playerIndex is incremented
        """
        if self.playerIndex + 1 < len(self.players):
            self.playerIndex += 1
            return True
        else:
            return False

    def gameOver(self):
        """
        Determina si el juego se ha acabado.

        returns: Verdadero si playerIndex >= el numero de jugadas, False de otra forma
        """
        return self.playerIndex >= len(self.players)

    def tryWord(self, word):

        if word == '.':
            raise EndHand()
        player = self.getCurrentPlayer()
        hand = player.getHand()
        if type(player) == ComputerPlayer:
            ps = player.getPossibleWord()
            word = player.pickBestWord(ps)
            if word == '.':
                raise EndHand()


        if self.wordlist.containsWord(word) and hand.containsLetters(word):
            points = getWordScore(word)
            player.addPoints(points)
            hand.update(word)
            if hand.isEmpty():
                raise EndHand()
            return points
        else:
            return None

    def getWinner(self):
        return max(self.players)

    def getNumPlayers(self):
        return len(self.players)

    def isTie(self):
        return len(self.players) > 1 and self.players[0].getScore() == self.players[1].getScore()

    def __str__(self):
        """
        Convierte este game object en un string

        returns: la concatenacion del string en representación de los jugadores
        """
        string = ''
        for player in self.players:
            string += str(player)
        return string